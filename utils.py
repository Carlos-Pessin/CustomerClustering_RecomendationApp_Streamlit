import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def make_recomendation_bycluster(client, n_itens=10):
    # import sparse & RFM matrix
    df_RFM_labeled = pd.read_csv('data/RFM_Labeled.csv').set_index('CustomerID')
    sparse_itens_client = pd.read_csv('data/sparse_itens_client.csv').set_index('CustomerID')

    # find similar clients and calculate recomendation
    cluster = df_RFM_labeled.loc[client]['Label']
    cluster_clients = df_RFM_labeled.query('Label==2').index
    recomendation = pd.DataFrame(sparse_itens_client.loc[cluster_clients].sum()).sort_values(by=0, ascending=False).nlargest(n=n_itens, columns=0).index.to_list()

    return recomendation


def make_recomendation_byitens(client, n_itens=10):
    # preprocessing
    client = str(client) + '.0'

    # import sparse & similarity matrix
    sparse_itens_client = pd.read_csv('data/sparse_itens_client.csv').set_index('CustomerID')
    similarity_matrix = pd.read_csv('data/similarity_matrix.csv').set_index('id')

    # find similar clients and calculate recomendation
    similar_clients = pd.DataFrame(similarity_matrix[client]).sort_values(by=client, ascending=False).reset_index().nlargest(n=31, columns=client)['id'].to_list()[1:]
    recomendation = pd.DataFrame(sparse_itens_client.loc[similar_clients].sum()).sort_values(by=0, ascending=False).nlargest(n=n_itens, columns=0).index.to_list()
    
    return recomendation