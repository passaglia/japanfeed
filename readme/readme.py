import pandas as pd
import os

LIST_FILE = os.path.join(os.path.dirname(__file__), "../list.csv")
TEMPLATE_FILE = os.path.join(os.path.dirname(__file__), "template.md")
README_FILE = os.path.join(os.path.dirname(__file__), "../README.md")

with open(TEMPLATE_FILE) as f:
    readme = f.read()

df = pd.read_csv(LIST_FILE, comment="#")
for tag in df["tag"].unique():
    formatted_list = ""
    for index, row in df.loc[df["tag"] == tag].iterrows():
        formatted_list += "- [" + row["name"] + "]" + "(" + row["url"] + ")"
        if not pd.isna(row["rss"]):
            formatted_list += " ([RSS]" + "(" + row["rss"] + ")" + ")"
        formatted_list += "\n"

    readme = readme.replace("$" + tag + "$", formatted_list)

with open(README_FILE, "w") as f:
    f.write(readme)
