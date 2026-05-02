import pandas as pd 

houses = pd.read_csv("data/kc_house_data.csv")
states = pd.read_csv("data/states.csv")
titanic = pd.read_csv("data/states.csv")
netflix = pd.read_csv("data/netflix_titles.csv",sep="|",index_col=0)
nst_est = pd.read_csv("data/nst-est2020.csv")
nst_est.columns = nst_est.columns.str.lower()
"""
Inspecting Dataframes

pd.options.display.min_rows = 15
print(houses.columns)

print(houses.head())

print(houses.tail())

print(houses.shape)

houses.info()
states.info()
print(titanic)
titanic.head()
"""
print(netflix)
print(nst_est)