import pandas as pd

bestsellers = pd.read_csv("data/bestsellers.csv")
print(bestsellers)

#1
booknames = bestsellers['Name']
user_ratings = bestsellers['User Rating']
first_eight_autors = bestsellers['Author'].head(8)

#2
genres_unique = bestsellers['Genre'].unique()
authors_unique = bestsellers['Author'].unique()
average_price = bestsellers['Price'].mean()
ten_highest_price = bestsellers['Price'].nlargest(10)

#3
top_three_common_titles = bestsellers['Name'].value_counts().head(3)
author_user = bestsellers[['Author','User Rating']]
author_user_mode = author_user.value_counts()
print(top_three_common_titles)