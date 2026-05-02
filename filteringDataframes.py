import pandas as pd 

titanic = pd.read_csv("data/titanic.csv")
houses = pd.read_csv('data/kc_house_data.csv')
netflix = pd.read_csv("data/netflix_titles.csv",sep="|",index_col=0)

#headT = titanic.head()
#bools = [True,False,True,True,True]
#print(headT.sex == 'female')
#print(headT[headT.sex == 'female'])
#print(headT[headT.survived == 0])
#print(headT[bools])

#print(titanic[titanic.survived == 1])
#print(titanic.info())
#print(titanic[titanic.age == '18'])
#print(titanic[titanic.pclass != 1].pclass.value_counts())
#print(houses[houses.price >= 6000000])
#print(houses[houses.bedrooms < 1])

#print(houses[houses["bedrooms"].between(2,4)])


#countries = ["India","Japan","South Korea"]
#rating = ['TV-MA','R']
#print(netflix[netflix.country.isin(countries)].country.value_counts())
#print(netflix[netflix.rating.isin(rating)].rating.value_counts())

#female_survived = (titanic.sex == 'female') & (titanic.survived == 1)
#waterfront_cheap = (houses['waterfront'] == 1) & (houses['price'] <= 500000)
#bestview_goodgrade = (houses['view'] == 4) & (houses['grade'] >= 11)
#print(titanic.info())
#print(titanic[female_survived])
#print(houses[waterfront_cheap])
#print(houses[bestview_goodgrade])

#renovated_build= (houses.yr_renovated >= 2014) | (houses.#yr_built >= 2014)
#recent_houses = houses[renovated_build] 
#print(recent_houses[['yr_renovated','yr_built']].sort_values(['yr_renovated'],ascending=False))

#df = titanic.head()
#women = titanic.sex == 'female'
#print(df[titanic.sex != women])

print(netflix.info())
print(netflix[netflix['director'].isna() & netflix['cast'].isna()])