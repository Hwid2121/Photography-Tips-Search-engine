import pyterrier as pt
import pandas as pd
import db_pandas as db
# Initialize PyTerrier if not started
if not pt.started():
    pt.init()

# Load your documents from the database
docs_df = db.docs_df

# Use the existing directory for the index
index_path = "./pd_index"

# Specify overwrite=True when creating the DFIndexer
pd_indexer = pt.DFIndexer(index_path, overwrite=True, verbose=False)
index_ref = pd_indexer.index(
    text=docs_df['title'] + ' ' + docs_df['content'],
    docno=docs_df['_id']
)

# Optionally, print information about the index
index = pt.IndexFactory.of(index_ref)
print(index.getCollectionStatistics().toString())

# Create BatchRetrieve with BM25 retrieval model and query expansion
br = pt.BatchRetrieve(index, wmodel="BM25", controls={"termpipelines": "Stopwords,PorterStemmer"})



# Define the query
query = "photo editing software"

def search_query(query):
    # Perform retrieval
    res = br.transform(query)

    # Sort the results by score, giving more priority to the title rank
    res = res.sort_values(by="score", ascending=False)

    # Filter documents based on the sorted results
    final_result = docs_df[docs_df["_id"].isin(res["docno"])]

    # Print and save the results
    print(res)
    print(final_result)
    res.to_csv("res.csv", index=False)
    final_result.to_csv("final_result.csv", index=False)

search_query(query)