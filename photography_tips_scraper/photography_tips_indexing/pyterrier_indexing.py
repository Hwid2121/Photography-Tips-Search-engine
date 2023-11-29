import pyterrier as pt
import db_pandas as db
import pandas as pd

if not pt.started():
    pt.init()

docs_df = db.docs_df

# Use the existing directory for the index
index_path = "./pd_index"

# Specify overwrite=True when creating the DFIndexer
pd_indexer = pt.DFIndexer(index_path, overwrite=True, verbose=True)
index_ref = pd_indexer.index(text=docs_df['content'], docno=docs_df['_id'])
# Optionally, print information about the index
index = pt.IndexFactory.of(index_ref)

print(index.getCollectionStatistics().toString())

# Create BatchRetrieve
br = pt.BatchRetrieve(index, wmodel="Tf")

# Perform a search
query = "photo editing software"
br.search(query)

# br.transform(query)
