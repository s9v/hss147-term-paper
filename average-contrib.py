import os, sys, codecs, json, operator
from bs4 import BeautifulSoup
import requests

users_file = 'users.txt'
print('Reading from ' + users_file)
with open(users_file, 'r') as f:
  users = json.load(f)

high = 0
nhigh = 0
low = 0
nlow = 0

for user in users:
  if 'rating' not in user:
    continue

  if user['rating'] <= 1600:
    low += user['contribution']
    nlow += 1
  elif user['rating'] >= 2000:
    high += user['contribution']
    nhigh += 1

print('avg high: ' + str(high/nhigh))
print('avg low: ' + str(low/nlow))