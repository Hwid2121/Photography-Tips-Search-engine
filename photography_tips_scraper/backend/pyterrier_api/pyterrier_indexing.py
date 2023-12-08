import pyterrier as pt
import pandas as pd
import json
import ast
import pymongo

index = None
docs_df = pd.DataFrame()

def mongodb_DF():
    global docs_df
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["informationRetrieval"]

    collection1_data = list(db["data_Website1"].find())
    collection2_data = list(db["data_Website2"].find())
    collection3_data = list(db["data_Website3"].find())

    df_collection1 = pd.DataFrame(collection1_data, columns=["title", "content", "article_tags", "_id", "url", "images_url"])
    df_collection2 = pd.DataFrame(collection2_data, columns=["title", "content", "article_tags", "_id", "url", "images_url"])
    df_collection3 = pd.DataFrame(collection3_data, columns=["title", "content", "article_tags", "_id", "url", "images_url"])

    docs_df = pd.concat([df_collection1, df_collection2, df_collection3], ignore_index=True)
    docs_df["_id"] = docs_df["_id"].astype(str)

    # Close MongoDB connection
    client.close()

def start_indexing():
    global index, docs_df

    if not pt.started():
        pt.init()

    # Use the existing directory for the index
    indexer = pt.DFIndexer("./index_3docs", overwrite=True)


    index_ref = indexer.index(
        text=docs_df["content"],
        docno=docs_df["_id"])

    index = pt.IndexFactory.of(index_ref)

def search_query(query):
    global index, docs_df

    # Initialize the BatchRetrieve object with the provided index and retrieval model
    br = pt.BatchRetrieve(index, num_result=5, wmodel="BM25")

    # Create a DataFrame with the query
    queries = pd.DataFrame([["q1", str(query)]], columns=["qid", "query"])

    # Retrieve results
    res = br.transform(queries)

    # Sort the results by score in descending order
    res = res.sort_values(by="score", ascending=False)

    # Get the document IDs of the top results
    docs_ids = []
    for i in range(res.shape[0]):
        tmp = res.iloc[i, :]
        docs_ids.append(tmp['docid'])
        if i >= 100:
            break

    # Retrieve the relevant fields for the documents
    docs_to_return = []
    for doc_id in docs_ids:
        if doc_id >= len(docs_df):
            doc = docs_df.iloc[doc_id - len(docs_df)]
        else:
            doc = docs_df.iloc[doc_id]
        docs_to_return.append({'title': doc['title'], 'content': doc['content'], 'url': doc['url'], 'article_tags': doc['article_tags']})

    return docs_to_return


def recommender(history):
    global index, docs_df

    # Check if history is empty or None
    if not history:
        print("Error: Empty or None history provided.")
        return []

    # # Convert the string representation of a list into an actual list
    # try:
    #     history_list = ast.literal_eval(history)
    # except (SyntaxError, ValueError) as e:
    #     print(f"Error: Failed to parse history string - {str(e)}")
    #     return []

    # # Check if index or docs_df is None
    # if index is None or docs_df is None:
    #     print("Error: Index or docs_df is not initialized.")
    #     return []

    # Convert the list of strings into a single space-separated query
    # history = history.replace('+', ' ')

    # query = ""
    # for ele in history:
    #     query += ele
     
 
    print("histo: ", history)

    # query = []
    query = " ".join(map(lambda ele: " ".join(ele.split("+")), history))

    # print("i am searching for:", query)
    # Initialize the BatchRetrieve object with the provided index and retrieval model
    br = pt.BatchRetrieve(index, num_result=5, wmodel="BM25")

    # Create a DataFrame with the query
    queries = pd.DataFrame([["q1", str(query)]], columns=["qid", "query"])

    try:
        # Retrieve results
        res = br.transform(queries)

        # Check if res is empty
        if res.empty:
            print("Warning: Empty result set.")
            return []

        # Sort the results by score in descending order
        res = res.sort_values(by="score", ascending=False)

        # Get the document IDs of the top results
        docs_ids = []
        for i in range(min(100, res.shape[0])):
            tmp = res.iloc[i, :]
            docs_ids.append(tmp['docid'])

        # Retrieve the relevant fields for the documents
        docs_to_return = []
        for doc_id in docs_ids:
            if doc_id >= len(docs_df):
                doc = docs_df.iloc[doc_id - len(docs_df)]
            else:
                doc = docs_df.iloc[doc_id]
            docs_to_return.append({'title': doc['title'], 'content': doc['content'], 'url': doc['url'], 'article_tags': doc['article_tags']})

        return docs_to_return

    except Exception as e:
        print(f"Error: An exception occurred - {str(e)}")
        return []
    

def init():
    mongodb_DF()
    start_indexing()
    print("Preparation Phase terminated.")

# Example usage:
init()

