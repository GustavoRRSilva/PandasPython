import pandas as pd
titanic = pd.read_csv("data/titanic.csv")
houses = pd.read_csv("data/kc_house_data.csv")
netflix = pd.read_csv("data/netflix_titles.csv",sep="|")
countries = pd.read_csv('data/world-happiness-report-2021.csv',index_col="Country name")
btc = pd.read_csv("data/coin_Bitcoin.csv")

#btc.drop(labels = ["Symbol","Name","SNo"],axis='columns')
#btc.drop(columns = ["Symbol","Name","SNo"])

#new_btc = btc[["Date","High","Low"]]

#print(new_btc)

#countries_drop_denmark = countries.drop(labels=["Denmark","Finland"],axis=0)
#print(countries_drop_denmark)

#countries_drop_first_three = countries.drop(countries.index[0:2])
#print(countries_drop_first_three)

#titanic["species"] = 'human'
#houses.insert(0,"country","King County")
#houses.insert(3,"num_bedrooms",houses["bedrooms"])



#titanic["num_relatives"] = titanic["sibsp"] + titanic["parch"]

#print(titanic[titanic["survived"] == 1 ].sort_values(["num_relatives"],ascending=False))

#houses["price_sqft"] = houses["price"] / houses["sqft_living"]
#print(houses.sort_values("price_sqft",ascending=False))
#print(houses.sort_values("price_sqft",ascending=False).head(50)["zipcode"].#value_counts())

btc["change"] = btc["Close"] - btc["Open"]

print(btc[["Date","Close","Open","change"]].sort_values("change",ascending=False))