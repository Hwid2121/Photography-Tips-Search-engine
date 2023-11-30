import pyterrier as pt
import db_pandas as db
import pandas as pd
import pyterrier_indexing as pti

# index = pti.index
# br = pt.BatchRetrieve(index, wmodel="Tf") #Alternative Models: "TF_IDF", "BM25"
#
# def query(query_string):
#     queries = pd.DataFrame([{'query': query_string}])
#     br.transform(queries)
#
#
# query("best photo editing software")
