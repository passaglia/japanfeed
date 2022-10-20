import pandas as pd
import os

LIST_FILE = os.path.join(os.path.dirname(__file__), "../list.csv")
OPML_FILE = os.path.join(os.path.dirname(__file__), "../list.opml")

header = """<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
	<head>
		<title>rss feeds from open-data-japan</title>
	</head>
	<body>
		"""

footer = """		
	</body>
</opml>"""

opmlstring = header

df = pd.read_csv(LIST_FILE, comment="#")
for tag in df["tag"].unique():
    empty = True
    for index, row in df.loc[df["tag"] == tag].iterrows():
        if not pd.isna(row["rss"]):
            if empty:
                opmlstring += """<outline text="{}">\n""".format(tag.title())
                empty = False
            opmlstring += """<outline text="{name}" type="rss" xmlUrl="{rss}" htmlUrl="{url}" description=""/>\n""".format(
                **row
            )
    if not empty:
        opmlstring += "</outline>\n"

opmlstring += footer

with open(OPML_FILE, "w") as f:
    f.write(opmlstring)
