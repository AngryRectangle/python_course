import sys
import requests
import json
import plotly.express as px
import pandas as pd
from collections import namedtuple

token_file = sys.argv[1]
ips_file = "ips.txt"
uncategorized = 'No data'
max_try = 5

token = open(token_file).readline()
ips = open(ips_file).readlines()
payload = {'token': token}
Key = namedtuple('Key', ['country', 'region', 'city'])
result = {}
tries = 0
for i in range(0, len(ips)):
    ip = ips[i]
    try:
        content = requests.get(f'https://ipinfo.io/{ip}', params=payload).content
    except:
        print("Fail to load")
        tries += 1
        if tries < max_try:
            print('Retry')
            i -= 1
            continue
        else:
            print('Abort')
            break
    decoded = json.loads(content)
    if 'country' not in decoded:
        key = Key(uncategorized, uncategorized, uncategorized)
    else:
        key = Key(decoded['country'], decoded['region'], decoded['city'])
    if key not in result:
        result[key] = 1
    else:
        result[key] += 1

if len(result) == 0:
    print('No info was obtained')
else:
    result = pd.DataFrame(
        {'country': key.country, 'region': key.region, 'city': key.city, 'count': value} for key, value in
        result.items())
    fig = px.sunburst(result, path=['country', 'region', 'city'], values='count', title='IP distribution over world')
    fig.show()
