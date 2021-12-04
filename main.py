import sys
import requests
import json
import plotly.express as px
import pandas as pd
from collections import namedtuple

token_file = sys.argv[1]
ips_file = "ips.txt"

token = open(token_file).readline()
ips = open(ips_file).readlines()
payload = {'token': token}
Key = namedtuple('Key', ['country', 'region', 'city'])
result = {}
for ip in ips:
    content = requests.get(f'https://ipinfo.io/{ip}', params=payload).content
    decoded = json.loads(content)
    key = Key(decoded['country'], decoded['region'], decoded['city'])
    if key not in result:
        result[key] = 1
    else:
        result[key] += 1

show = list(
    {'country': key.country, 'region': key.region, 'city': key.city, 'count': value} for key, value in result.items())
fig = px.sunburst(pd.DataFrame(show), path=['country', 'region', 'city'], values='count')
fig.show()
