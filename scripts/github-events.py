# Lab 3 Scripts   
#!/Users/angelikabaloy/DS-2002-Spr25/.venv/bin/python3

import os
import json
import requests

# retrieving env var
GHUSER = os.getenv('GITHUB_USER')
print(GHUSER)

# defining url 
url = 'https://api.github.com/users/{0}/events'.format(GHUSER)
print(url)

# fetch recent github activity
r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)

print(r)