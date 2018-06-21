import os, sys, codecs, json, operator
from bs4 import BeautifulSoup

authors = set()

for i in range(40001, 60001):
  if i % 500 == 0:
    print('Analyzing ' + str(i))
  path = os.path.join('data', 'blog-{blogid}.json'.format(blogid=i))
  with codecs.open(path, 'r', 'utf-8') as f:
    data = json.load(f)

  if data['status'] != 'OK':
    continue

  if data['result']['locale'] != 'en':
    continue

  handle = data['result']['authorHandle']
  authors.add(handle)

print(len(authors))
authors = list(authors)

authors_file = 'authors-url.txt'
print('Writing to ' + authors_file)
with open(authors_file, 'w') as f:
  n = 200
  for i in range(0, len(authors), n):
    f.write(';'.join(authors[i:i+n]) + '\n')