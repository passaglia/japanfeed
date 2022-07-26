import os
import pandas
import uuid
import json

uuid.uuid4()

GITHUB_FILE = '../lists/githubs.csv'
WEBSITES_FILE = '../lists/websites.csv'
PORTALS_FILE = '../lists/portals.csv'
PUBLICATIONS_FILE = '../lists/publications.csv'

JSON_FILE = './data/url-watches.json'

with open(JSON_FILE) as f:
    json_string = f.read()

json_dict = json.loads(json_string)
tracked_urls = []
for databaseid in json_dict['watching'].keys():
    url = json_dict['watching'][databaseid]['url']
    tracked_urls.append(url)

websites_df = pandas.read_csv(WEBSITES_FILE)
entry_list = []
for index, row in websites_df.iterrows():
    if row['url'] not in tracked_urls:
        print(row['url'])
        entry = {
            'url': row['url'],
            'tag': 'website',
            'title': row['name']
        }
        new_id = str(uuid.uuid4())
        json_dict['watching'][new_id] = entry

portals_df = pandas.read_csv(PORTALS_FILE)
entry_list = []
for index, row in portals_df.iterrows():
    if row['url'] not in tracked_urls:
        print(row['url'])
        entry = {
            'url': row['url'],
            'tag': 'portal',
            'title': row['name']
        }
        new_id = str(uuid.uuid4())
        json_dict['watching'][new_id] = entry

publications_df = pandas.read_csv(PUBLICATIONS_FILE)
entry_list = []
for index, row in publications_df.iterrows():
    if row['url'] not in tracked_urls:
        print(row['url'])
        entry = {
            'url': row['url'],
            'tag': 'publication',
            'title': row['name']
        }
        new_id = str(uuid.uuid4())
        json_dict['watching'][new_id] = entry

json_string = json.dumps(json_dict)
with open(JSON_FILE, 'w') as f:
    f.write(json_string)

