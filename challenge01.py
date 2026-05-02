import pandas as pd
bestseller = pd.read_csv("data/bestsellers.csv")

print(bestseller.describe(include="O"))

print(bestseller.tail().describe())
print(bestseller.sum())
print(bestseller.count())
print(bestseller.max())
print(bestseller.mode())