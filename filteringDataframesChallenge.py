import pandas as pd 


#Find the books written by Pete Souza
# Find the books that are under 10 dollars
#Find the books that have a price between 50 and 60 dollars
#Find all the books written by Kristin Hannah, Andy Weir, or Delia Owens
#Find the Non Fiction books that are rated 4.9
#Find the fiction book with the lowest User Rating
#Find 2012's top 5 Fiction books with the most Reviews
bestsellers = pd.read_csv('data/bestsellers.csv')
pete_souza = bestsellers.Author == 'Pete Souza'
under_dollars = bestsellers.Price <= 10
price_between = bestsellers.Price.between(50,60)
multiple_authors = bestsellers.Author.isin(['Kristin Hannah','Andy Weir','Delia Owens'])
nonfiction_rate = (bestsellers.Genre == 'Non Fiction') & (bestsellers['User Rating'] == 4.9)
fiction_lowest = bestsellers[bestsellers.Genre == 'Fiction'].sort_values(['User Rating'],ascending=True).head(1)
fiction_reviews = bestsellers[(bestsellers.Genre == 'Fiction') & (bestsellers.Year == 2012)].sort_values(['Reviews'],ascending=False).head(5)
print(fiction_reviews)
print(bestsellers[pete_souza])
print(bestsellers[under_dollars])
print(bestsellers[price_between])
print(bestsellers[multiple_authors])
print(bestsellers[nonfiction_rate])