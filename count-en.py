import os, codecs, json

ru = 0
en = 0
bad = 0

for i in range(55001, 60001):
  path = os.path.join('data', 'blog-{blogid}.json'.format(blogid=i))
  with codecs.open(path, 'r', 'utf-8') as f:
    data = json.load(f)

  if data['status'] != 'OK':
    bad += 1
    continue

  if data['result']['locale'] == 'ru':
    ru += 1
  elif data['result']['locale'] == 'en':
    en += 1
  else:
    print('(??) {blogid} has locale {locale}'.format(blogid=i, locale=data['result']['locale']))

print('bad: {bad}'.format(bad=bad))
print('ru: {ru}'.format(ru=ru))
print('en: {en}'.format(en=en))