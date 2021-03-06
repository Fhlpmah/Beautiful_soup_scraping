from dataclasses import field
from bs4 import BeautifulSoup
import csv
import requests

web_page = requests.get(
    'https://www.basketball-reference.com/players/d/doncilu01/gamelog/2022').text
soup = BeautifulSoup(web_page, 'lxml')

# only use for debugging test
# box = soup.find('div', class_='table_container')
# print(box)

# csv writing tool ( in binary mode so the data wont changed )
file = open('LukaDoncic2022GameLogs.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(file)

# header
writer.writerow(['date', 'field_goal',
                 'field_goal_attempt', 'field_goal_pct', 'point'])

for numbers in range(200, 248):
    stats = soup.find_all('tr', attrs={'id': f'pgl_basic.{numbers}'})
    for stat in stats:
        date = stat.find('td', class_='left', attrs={
                         'data-stat': 'date_game'}).a.text
        field_goal = stat.find('td', class_='right', attrs={
                               'data-stat': 'fg'}).text
        field_goal_attempt = stat.find('td', class_='right', attrs={
                                       'data-stat': 'fga'}).text
        field_goal_pct = stat.find('td', class_='right', attrs={
                                   'data-stat': 'fg_pct'}).text
        point = stat.find('td', class_='right', attrs={
                          'data-stat': 'pts'}).text

        print(date + ' ' + field_goal + ' ' + field_goal_attempt +
              ' ' + field_goal_pct + ' ' + point)

        writer.writerow([date, field_goal, field_goal_attempt, field_goal_pct, point])



file.close()
