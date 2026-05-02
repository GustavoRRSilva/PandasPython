import pandas as pd

#Part 1
#pokemon = pd.read_csv("data/Pokemon.csv",index_col='Name')
#print(pokemon)

#Part 2
#pokemon = pd.read_csv("data/Pokemon.csv",index_col=['Name'])
#pokemon.sort_values('Num', ascending=True, inplace=True) 
#print(pokemon.sort_index(ascending=True))
#print(pokemon.sort_values(['Total','Attack'],ascending=False))
#print(pokemon)

#Part 3 
pokemon = pd.read_csv("data/Pokemon.csv")
#print(pokemon['Speed'].sort_values(ascending=False).head(10).mean())
print(pokemon.sort_values(['Attack'],ascending=False).head(20)['Type 1'].value_counts().index[0])

#Part 4 
#pokemon = pd.read_csv("data/Pokemon.csv",index_col='Name')
#fish_pokemon = ['Magikarp','Goldeen','Horsea','Seaking','Seadra','Gyarados']
#print(pokemon.loc[['Diglett']])
#print(pokemon.loc[['Eevee','Vulpix']])
#print(pokemon.sort_index(ascending=True).loc['Charizard':'Charmeleon'])
#print(pokemon.iloc[[30,40,50]])
#print(pokemon.loc[fish_pokemon])