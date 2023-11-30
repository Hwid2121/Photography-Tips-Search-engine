import pyterrier as pt
import db_pandas as db
import pandas as pd

if not pt.started():
    pt.init()

docs_df = db.docs_df

# Use the existing directory for the index
index_path = "./pd_index"

# Specify overwrite=True when creating the DFIndexer
pd_indexer = pt.DFIndexer(index_path, overwrite=True, verbose=False)
index_ref = pd_indexer.index(
    text=docs_df['content']
, docno=docs_df['_id'])
# Optionally, print information about the index
index = pt.IndexFactory.of(index_ref)

print(index.getCollectionStatistics().toString())

# Create BatchRetrieve
br = pt.BatchRetrieve(index, wmodel="Tf")

query = "photo editing software"
query = [[str(i+1), e] for i, e in enumerate(query.split(" "))]
topics = pd.DataFrame(query, columns=["qid", "query"])
res = br.transform(topics)

final_result = docs_df[docs_df["_id"].isin(res["docno"])]
# final_result_title = final_result[["title"]]
# final_result contine cio che vuoi

print(res)
print(final_result)
res.to_csv("res.csv")
final_result.to_csv("final_result.csv")

# Perform a search
# query = "photo editing software"
# br.search(query)

# Install pyenv
# pyenv virtualenv name_of_venv
# source ... activate venv
# VS code python select interpreter
# requirements.txt
# pip install -r requirements.txt
# Controllare il VENV: pip -V


# Scrapy==2.11.0
# python-terrier==0.10.0
# pandas==2.0.3


# pip freeze | grep name_of_package