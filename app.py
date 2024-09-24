import streamlit as st
import utils

# Page config
st.set_page_config(page_title='Product recomendation')
st.title('Product recomendation')

st.markdown(
    """
## Challenge 7 - Customer Clustering and Product Recomendation
From the database, customers were grouped according to the FM metrics:
- F: Frequency = number of purchases made by the customer
- M: Mean Ticket = average value of the customer's purchases

Three groups were created, which can be observed in the graph below:

    """
)

st.image('data/clusters.png')

st.markdown(
    """
The main characteristics of the groups are:
- 0: Customers who purchase with higher Frequency but lower Mean Ticket;
- 1: Customers who purchase with higher Mean Ticket but low Frequency;
- 2: Customers who purchase with low Frequency and Mean Ticket.

Another approach consisted of grouping customers according to the items they purchased, that is, customers who bought more similar products were grouped.

Below you can generate product recommendations for a customer based on the consumption of other customers using the two methods defined above.
    """
)

# -- Paramerters -- #
client = st.number_input(label='Inform the client to calculate recomendations', value=17908)
n_itens = st.slider(label='How many recomendations do you want?', min_value=1, max_value=50)
method = st.selectbox(label='Choose method', options=['RFM','Itens bought'])


# -- Model -- #
if method == 'RFM':
    recomendations = utils.make_recomendation_bycluster(client=client, n_itens=n_itens)
else:
    recomendations = utils.make_recomendation_byitens(client=client, n_itens=n_itens)

st.success(f'These are the top {n_itens:.2f} recomendations')
st.table(data=recomendations)


st.markdown(
    """
## Suggestions

    This analisys shows that the most profitable cluster is the one labeled 0 (High Frequency and smaller Mean Ticket), followed by clusters 1 and 2. In fact, cluster 0 clients spent 7 times more in average than cluster 1 and 14 times more than cluster 2 clients.

    Therefore, the company can increase its earnings by increasing frequency of purchases, so it would be interest for the company to set strategies to retain customers, even if it requires to reduce prices. 

    Another strategy is to implement a recomendation system to the company's website, as described before.
    """
)