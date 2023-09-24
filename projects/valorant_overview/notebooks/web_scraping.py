import requests
from bs4 import BeautifulSoup
import csv

urls = [
    'https://www.esportsearnings.com/history/2023/games/646-valorant',
    'https://www.esportsearnings.com/history/2023/games/646-valorant/top_players_100',
    'https://www.esportsearnings.com/history/2023/games/646-valorant/top_players_200',
    'https://www.esportsearnings.com/history/2023/games/646-valorant/top_players_300',
    'https://www.esportsearnings.com/history/2023/games/646-valorant/top_players_400',
]

responses = []

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        responses.append(response)
    else:
        raise Exception(f'Não foi possível encontrar a página {url}')

data = []

for response in responses:
    soup = BeautifulSoup(response.content, 'html.parser')
    tbody = soup.find('tbody')

    for row in tbody.find_all('tr'):
        row_data = []

        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())

        data.append(row_data)


csv_file = '../data/dataset2.csv'


with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    header = ['ID', 'Nick', 'Name', 'Total (year)', 'Total (Game)', '% of Game', 'Total (Overall)', '% of Overall']
    writer.writerow(header)

    for row in data:
        writer.writerow(row)