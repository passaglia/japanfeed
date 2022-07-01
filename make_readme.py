import os 
import pandas

GITHUB_FILE = './lists/githubs.csv'
WEBSITES_FILE = './lists/websites.csv'
TEMPLATE_FILE = './template.md'
README_FILE = './README.md'

gh_df = pandas.read_csv(GITHUB_FILE)
formatted_github_list = ''
for index, row in gh_df.iterrows():
    formatted_github_list += '- ['+row['name']+']'+'('+row['url']+')\n'

websites_df = pandas.read_csv(WEBSITES_FILE)
formatted_websites_list = ''
for index, row in websites_df.iterrows():
    formatted_websites_list += '- ['+row['name']+']'+'('+row['url']+')\n'


with open(TEMPLATE_FILE) as f:
    template = f.read()

readme = template.replace('$GITHUBS$', formatted_github_list)
readme = readme.replace('$WEBSITES$', formatted_websites_list)

with open(README_FILE,'w') as f:
    f.write(readme)