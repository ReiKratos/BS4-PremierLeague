import urllib.request
from bs4 import BeautifulSoup

#finding teams tag by attribute 'data-filtered-table-row-name'
def has_row_name(tag):
	return tag.has_attr('class') and tag.has_attr('data-filtered-table-row-name')


with urllib.request.urlopen('https://www.premierleague.com/tables') as page:
	soup = BeautifulSoup(page, 'html.parser')

#Getting all 20 teams' tag
table = soup.findAll(has_row_name, limit=20)

print('\n\n{:>25} {:>25} {:>25}'.format('TEAM', 'RANK', 'POINTS'))

#each iteration is a team tag
for i in range((len(table))):
	team_name = table[i]["data-filtered-table-row-name"]

	for td in table[i].find('td', attrs={'class':'points'}):
		team_info = [team_name, i+1, td]
		print('{:>25} {:>25} {:>25}'.format(*team_info))

