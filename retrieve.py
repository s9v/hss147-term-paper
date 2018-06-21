import requests
import os
import time
import codecs

for blog_id in range(12487, 999, -1):
  # Sleep to limit API calls to 5/s
  print('Sleeping (0.21s)\n')
  time.sleep(0.21)

  # Call API
  print('Downloading: ' + str(blog_id))
  r = requests.get('http://codeforces.com/api/blogEntry.view?blogEntryId={blog_id}'.format(blog_id=blog_id))

  
  if r.status_code != 200:
    print('blog_id: ' + str(blog_id))
    print('r.status_code: ' + str(r.status_code))
    print('r.content: ' + str(r.content))
    # continue

  # Write data  
  with codecs.open(os.path.join('data', 'blog-{blog_id}.json'.format(blog_id=blog_id)), 'w', 'utf-8') as f:
    data = r.content.decode()
    f.write(data)

  