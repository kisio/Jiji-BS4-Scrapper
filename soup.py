import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

URL = "https://jiji.co.ke/vehicles"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# find all div tags with the class "sc-1fcmfeb-2 gCVEnI"
divs = soup.find_all('div', class_='sc-1fcmfeb-2 gCVEnI')

# create a list of tuples (name, price) for each car
cars = []
for div in divs:
    name = div.find('a', class_='sc-1fcmfeb-3 iUMmLg').text
    price = div.find('div', class_='sc-1fcmfeb-4 fbTIMe').text
    cars.append((name, price))

# create a pandas DataFrame from the list of tuples
df = pd.DataFrame(cars, columns=['Name', 'Price'])

# save the DataFrame to an Excel file
df.to_excel("results.xlsx", index=False)
