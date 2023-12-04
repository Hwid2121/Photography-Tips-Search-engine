import pyterrier as pt
# import db_pandas as db
import pandas as pd
from pyterrier_indexing import search_query

def query(query_string):
    search_query(query=query_string)

#
# query("best photo editing software")


def test (query):
    return  query+ "/ciao test va"