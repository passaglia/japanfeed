import pandas as pd

LIST_FILE = "../list.csv"
OPML_FILE = "../list.opml"

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


# """<outline text="Twitter Lists" "></outline>"""


# OPML_OUTLINE_FEED = '<outline text="%(title)s" title="%(title)s" type="rss" version="RSS" htmlUrl="%(html_url)s" xmlUrl="%(xml_url)s" />'

# import sys
# import urllib2

# try:
# 	import json
# except ImportError:
# 	import simplejson as json

# def get_lists(url):
# 	request = urllib2.Request(url)
# 	request.add_header('User-Agent', '%s/%s +%s' % (
# 		__project_name__, __version__, __project_link__
# 	))
# 	opener = urllib2.build_opener()
# 	data = opener.open(request).read()
# 	return json.loads(data)

# def main(username):
# 	t_lists = get_lists(TWITTER_LISTS_URL % {'username': username})

# 	print OPML_START

# 	for t_list in t_lists['lists']:
# 		list_title = t_list['name']
# 		list_html_url = TWITTER_LIST_HTML_URL % {'username': username, 'list': t_list['slug']}
# 		list_xml_url = TWITTER_LIST_FEED_URL % {'username': username, 'list': t_list['slug']}
# 		print OPML_OUTLINE_FEED % {'title': list_title, 'html_url': list_html_url, 'xml_url': list_xml_url}

# 	print OPML_END

# if __name__ == "__main__":
# 	username = sys.argv[-1]
# 	main(username)
