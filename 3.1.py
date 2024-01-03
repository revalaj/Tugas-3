import pandas as pd

last_names = ['Connor', 'Connor', 'Reese']
first_names = ['Sarah', 'John', 'Kyle']
df = pd.DataFrame({
  'first_name': first_names,
  'last_name': last_names,
})

url = "https://github.com/luminati-io/Instagram-dataset-samples/raw/main/Instagram%20Profiles%20-%20Github%20Hashtag.xlsx"
database = pd.read_excel(url)
'''pd.read_csv('data.csv')'''
print(database.columns)
print(database.describe())
print(database.head())
print(database.tail())