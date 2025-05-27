# Original Vegetables Dataset by Rudra Prasad Bhuyan:
# https://www.kaggle.com/datasets/rudraprasadbhuyan/vegetables-dataset


import pandas as pd
import json


pd.set_option("display.max_columns", 15)

df = pd.read_csv("vegetablesDataset.csv")
print(df.head(20))

# for filtering, we only need the Name, Season, and Category, so drop the others
to_drop = ['Vegetable ID', 'Scientific Name', 'Color',
       'Origin', 'Nutritional Value (per 100g)',
       'Price (per kg)', 'Availability', 'Shelf Life (days)',
       'Storage Requirements', 'Growing Conditions', 'Health Benefits',
       'Common Varieties']
df.drop(columns=to_drop, inplace=True)

# we only need each veggie once
df.drop_duplicates(inplace=True)

# for correct filtering, only use season names
df.replace("Year-round", "Spring/Summer/Fall/Winter", inplace=True)
df["Season"] = df["Season"].str.lower()

veg_data = df.to_json(orient="records")
veg_data = json.loads(veg_data)

# split the seasons data into lists of seasons
for veg in veg_data:
    seasons = veg["Season"].split("/")
    veg["Season"] = seasons

output = open("vegetable_data.json", "w")
json.dump(veg_data, output)
output.close()
# for use with the microservice server, this file should be moved to 
# the main directory if it was not already saved there