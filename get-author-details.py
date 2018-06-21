import os, sys, codecs, json, operator
from bs4 import BeautifulSoup
import requests

authors_file = 'authors-url.txt'
print('Reading from ' + authors_file)
with open(authors_file, 'r') as f:
  lines = f.readlines()

users = []
for line in lines:
  authors = line.strip()
  r = requests.get('http://codeforces.com/api/user.info?handles={authors}'.format(authors=authors))
  print(r.status_code)
  data = json.loads(r.content)
  users.extend(data['result'])

users_file = 'users.txt'
with open(users_file, 'w') as f:
  json.dump(users, f)
