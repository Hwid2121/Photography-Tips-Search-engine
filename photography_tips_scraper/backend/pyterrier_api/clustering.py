import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pyterrier_indexing import docs_df

# Download NLTK punkt if not already downloaded
nltk.download('punkt')

# dataset = docs_df
dataset = docs_df.head(100)


texts = dataset.apply(lambda row: row['title'] + ' ' + row['content'], axis=1)

print("texts", texts)

def cleaned_func(text):
    # Remove regular expression (Some of them implemented for the specific task)
    text = re.sub(r'\(.*?\)', '', text)  # remove elements inside ()
    text = re.sub(r'\[.*?\]', '', text)  # remove elements inside []
    text = re.sub(r'\\', '', text)  # remove \
    text = re.sub(r'-', '', text)  # remove -
    text = re.sub(r'\n', '', text)  # remove
    text = re.sub(r'\s+', ' ', text).strip()  # Remove multiple spaces at the beginning and at the end of the sentences

    return text

# Apply function for each element (document) in the list
cleaned_texts = [cleaned_func(str(text)) for text in texts]

stemmer = PorterStemmer()

def apply_stem(text, stemmer):
    words = word_tokenize(text)
    stemmed_text = ' '.join([stemmer.stem(word) for word in words])
    return stemmed_text

stemmed_text = [apply_stem(str(text), stemmer) for text in texts]
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.9, min_df=0.01, max_features=1000)

X = vectorizer.fit_transform(stemmed_text)

# K-Means
n_clusters = 3  # set the number of clusters that you want
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)

clustering_labels = kmeans.labels_  # clustering labels

pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())  # TF-IDF Dataframe

def clustering_visualization(X, clustering_labels):
    tsne = TSNE(random_state=0)
    X_reduced = tsne.fit_transform(X.toarray())

    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=clustering_labels, cmap='viridis')
    plt.title('Clusters Visualization')
    plt.show()

clustering_visualization(X, clustering_labels)
