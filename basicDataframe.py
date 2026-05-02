import pandas as pd 

houses = pd.read_csv("data/kc_house_data.csv")
states = pd.read_csv("data/states.csv")
titanic = pd.read_csv("data/titanic.csv")
netflix = pd.read_csv("data/netflix_titles.csv",sep="|",index_col=0)
nst_est = pd.read_csv("data/nst-est2020.csv")
nst_est.columns = nst_est.columns.str.lower()

#The minimum of every column 
#print(houses.min())

#The max of every column 
#print(houses.max())

#The sum of every column 
#print(houses.sum(numeric_only=True))

#nst_est.tail(52).head(51).sum(numeric_only=True)
#print(titanic.count())
#print(netflix.count())


#print(houses.mean(numeric_only=True))
#print(houses.mode(numeric_only=True))
#print(houses.median(numeric_only=True))

#print(houses.describe())
#print(titanic.describe(include=["object","int64"]))
print(netflix.shape())
#print(titanic.name.replace("Zabour, Miss. Hileni","Gustavinho"))
#print(titanic.merge(netflix,left_on="ticket",right_on='on'))