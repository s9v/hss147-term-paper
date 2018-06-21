import os, sys, codecs, json, operator
from bs4 import BeautifulSoup
import requests

categories = {
  'profanity': ['fuck', 'fucking', 'shit', ''],
  'mild-profanity': ['hell', 'heck', 'damn']
}


# Read list of users
users_file = 'users.txt'
print('Reading from ' + users_file)
with open(users_file, 'r') as f:
  _users = json.load(f)

users = dict()
for user in _users:
  users[user['handle']] = user


# Blog id generator
def blogids():
  # for i in range(1, 20001):
  #   yield i
  for i in range(40001, 60001):
    yield i

# Read words one by one
words = dict()

for i in blogids():
  if i % 1000 == 0:
    print('Analyzing ' + str(i))
  path = os.path.join('data', 'blog-{blogid}.json'.format(blogid=i))
  with codecs.open(path, 'r', 'utf-8') as f:
    data = json.load(f)

  if data['status'] != 'OK':
    continue

  if data['result']['locale'] != 'en':
    continue

  content = data['result']['content']

  try:
    content = content.encode().decode('unicode-escape', errors='ignore')
  except UnicodeDecodeError:
    print(i)
    print(content)
    raise

  soup = BeautifulSoup(content, 'html.parser')
  text = soup.get_text(separator=' ')

  cur = ''
  latin = True
  for idx, c in enumerate(text):
    if c.isalpha():
      c = c.lower()
      cur += c
      if ord(c) < ord('a') or ord('z') < ord(c):
        latin = False
    else:
      if cur != '' and latin:
        handle = data['result']['authorHandle']
        # Extra filter: only words of users s.t. rating >= 2600
        if 'rating' in users[handle] and users[handle]['rating'] >= 2600:
          words[cur] = words.get(cur, 0) + 1
      cur = ''
      latin = True

sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
csv_file = 'words-separator.csv'
print('Writing to ' + csv_file)
with codecs.open(csv_file, 'w', 'utf-8') as f:
  for word, count in sorted_words:
    f.write('{word}, {count}\n'.format(word=word, count=count))