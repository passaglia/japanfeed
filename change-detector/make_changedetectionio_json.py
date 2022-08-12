import os
import pandas
import uuid
import json

uuid.uuid4()

LIST_FILE = '../list.csv'

JSON_FILE = './data/url-watches.json'

with open(JSON_FILE) as f:
    json_string = f.read()

json_dict = json.loads(json_string)
tracked_urls = []
for databaseid in json_dict['watching'].keys():
    url = json_dict['watching'][databaseid]['url']
    tracked_urls.append(url)

df = pandas.read_csv(LIST_FILE,comment='#')
entry_list = []
for index, row in df.iterrows():
    if row['tag'] != 'github':
        if row['url'] not in tracked_urls:
            print(row['url'])
            entry = {
                'url': row['url'],
                'tag': row['tag']+'s',
                'title': row['name']
            }
            new_id = str(uuid.uuid4())
            json_dict['watching'][new_id] = entry

json_string = json.dumps(json_dict)
with open(JSON_FILE, 'w') as f:
    f.write(json_string)

