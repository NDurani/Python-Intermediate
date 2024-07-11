import csv
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240710.csv")
color_column = data["Primary Fur Color"]

gray = 0
black = 0
cinnamon = 0

for color in color_column:
    if color == "Gray":
        gray += 1
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1

data_dict = {
    "colors": ["Gray", "Black", "Cinnamon"],
    "color_count": [gray, black, cinnamon]
             }

output_data = pandas.DataFrame(data_dict)
output_data.to_csv("my_data.csv")