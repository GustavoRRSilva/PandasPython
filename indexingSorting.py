import pandas as pd 

#btc = pd.read_csv("data/coin_Bitcoin.csv")
#btc.set_index("Date",inplace=True)
#print(btc)

#happiness = pd.read_csv('data/world-happiness-report-2021.csv')
#happiness.set_index("Country name",inplace=True)
#print(happiness['Healthy life expectancy'].head())

#countries = pd.read_csv('data/world-happiness-report-2021.csv',index_col="Country name")
#countries.sort_values("Healthy life expectancy",ascending=False,inplace=True)
#print(countries)

#houses = pd.read_csv('data/kc_house_data.csv')
#houses.sort_values(['bedrooms','bathrooms'],inplace=True,ascending=False)
#print(houses)

#titanic = pd.read_csv('data/titanic.csv')
#top_ten_titanic = titanic.head(10)
#top_ten_titanic.sort_values("name",key=lambda col: col.str.lower())
#print(top_ten_titanic)

#countries = pd.read_csv('data/world-happiness-report-2021.csv',index_col="Country name")
#countries.sort_index(ascending=False,inplace=True)


#countries = pd.read_csv('data/world-happiness-report-2021.csv',index_col="Country name")
#titanic = pd.read_csv('data/titanic.csv')
#print(countries.loc["Yemen"])
#print(countries.loc[["Yemen"]])
#print(countries.loc[["Canada","Mexico","United States"]])
#print(titanic.loc[[7,9]])
#print(titanic.loc[7:9])
#print(titanic.loc[7:9:8])
#print(countries.sort_index(inplace=False).loc["Denmark":"France"])

#countries = pd.read_csv('data/world-happiness-report-2021.csv',index_col="Country name")
#print(countries.iloc[[1,2,3]])

houses = pd.read_csv('data/kc_house_data.csv')
print(houses.loc[1:4,['price','bedrooms']])