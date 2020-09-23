import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.1016&lon=-118.3371#.X2uYLZP7Tlw')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

period_name = [i.find(class_='period-name').get_text() for i in items]
short_desc = [i.find(class_='short-desc').get_text() for i in items]
temp = [i.find(class_='temp').get_text() for i in items]

data = pd.DataFrame({'period_name':period_name,'short_desc':short_desc,'temp':temp})
# print(data)
# data.to_csv('weather.csv', index=False)
