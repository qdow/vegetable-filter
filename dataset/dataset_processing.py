# Original Vegetables Dataset by Rudra Prasad Bhuyan:
# https://www.kaggle.com/datasets/rudraprasadbhuyan/vegetables-dataset


import pandas as pd


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


df.to_json("vegetable_data.json", orient="records")
# for use with the microservice server, this file is then moved to the main directory
