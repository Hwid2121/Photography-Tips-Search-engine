import pandas as pd
import pymongoDB as db
import pandas as pd

# Assuming db.collection1_data, db.collection2_data, and db.collection3_data are lists or iterables
df_collection1 = pd.DataFrame(db.collection1_data, columns=["title", "content", "article_tags", "_id"])
df_collection2 = pd.DataFrame(db.collection2_data, columns=["title", "content", "article_tags", "_id"])
df_collection3 = pd.DataFrame(db.collection3_data, columns=["title", "content", "article_tags", "_id"])


# Concatenate DataFrames
docs_df = pd.concat([df_collection1, df_collection2, df_collection3], ignore_index=True)
docs_df["_id"] = docs_df["_id"].astype(str)

# print(docs_df["_id"])
# print(df)

# Drop duplicates
# df.drop_duplicates(subset=['url'], inplace=True)
