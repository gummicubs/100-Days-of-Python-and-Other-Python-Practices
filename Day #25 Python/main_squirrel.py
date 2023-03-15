import csv
import pandas

# with open('weather_data.csv') as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

data = pandas.DataFrame(pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'))

print(data['Primary Fur Color'].value_counts())