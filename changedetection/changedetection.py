import os
import pandas as pd
import uuid
import json
import subprocess
from time import sleep

LIST_FILE = "../list.csv"

DATA_FOLDER = "./data/"
JSON_FILE = DATA_FOLDER + "url-watches.json"

# if first time running
if not os.path.exists(DATA_FOLDER):
    # run change detection once
    bashCommand = "changedetection.io -C -d data/ -h 127.0.0.1 -p 5000"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    sleep(5)
    # open the json file once it is created
    while True:
        print("waiting for file to create")
        sleep(5)
        if os.path.exists(JSON_FILE):
            print("file has created, killing process")
            sleep(5)
            process.kill()

            # loading file
            with open(JSON_FILE) as f:
                json_string = f.read()
            json_dict = json.loads(json_string)

            # purge the default stuff
            json_dict["watching"] = {}

            # set default settings

            # replace file
            with open(JSON_FILE, "w") as f:
                f.write(json.dumps(json_dict))

            print("wrote file")

            break

# now put any new websites in watch list
with open(JSON_FILE) as f:
    json_string = f.read()

json_dict = json.loads(json_string)
tracked_urls = []
for databaseid in json_dict["watching"].keys():
    url = json_dict["watching"][databaseid]["url"]
    tracked_urls.append(url)

df = pd.read_csv(LIST_FILE, comment="#")
entry_list = []
for index, row in df.iterrows():
    if (row["tag"] != "github") and (pd.isna(row["rss"])):
        if row["url"] not in tracked_urls:
            print(row["url"])
            entry = {"url": row["url"], "tag": row["tag"], "title": row["name"]}
            new_id = str(uuid.uuid4())
            json_dict["watching"][new_id] = entry

with open(JSON_FILE, "w") as f:
    f.write(json.dumps(json_dict))

# # run change detection
# bashCommand = "changedetection.io -C -d data/ -h 127.0.0.1 -p 5000"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# sleep(10)

# # launch chrome
# bashCommand = """open -na "Google Chrome" --args --incognito http://127.0.0.1:5000/"""
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
