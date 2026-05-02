import pandas as pd 

titanic = pd.read_csv("data/titanic.csv")
houses = pd.read_csv("data/kc_house_data.csv")
netflix = pd.read_csv("data/netflix_titles.csv",sep="|")
mystery_column = 'age'
#print(titanic.age)
#print(titanic['age'])
#print (titanic[mystery_column])
mins = houses.min(numeric_only=True)
#print(mins.index)
#print(mins.values)
#print(mins.shape)

bedrooms = houses.bedrooms
#print(bedrooms.head())
#print(bedrooms.tail())
#print(bedrooms.unique())
#print(bedrooms.nunique(dropna=False))
#print(bedrooms.nlargest(10))
#print(bedrooms.nsmallest(10,keep='all'))
#print(bedrooms.value_counts(ascending=True))
#print(houses.nlargest(10,["bedrooms",'bathrooms']))
#print(netflix[["title","rating"]])
#print(netflix[["title","rating"]].describe())

print(houses.bedrooms.plot())

