import pandas as pd

biden = pd.read_csv("data/JoeBidenTweets.csv",index_col='id')
drop_url = biden.drop(columns=['url'])
rop_row = biden.drop(361388562)
biden["user"] = "Joe Biden"
biden["ratio"] = biden["replies"] / biden["retweets"]
top_10_ratio = biden.sort_values("ratio",ascending=False).head(10)
biden["interactions"] = biden["replies"] + biden["retweets"] + biden["quotes"] + biden["likes"]
top_10_interactions = biden.sort_values("interactions",ascending=False).head(8)


