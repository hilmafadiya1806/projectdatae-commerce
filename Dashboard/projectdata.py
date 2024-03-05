import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

def create_review_df(df):
    review_df = df.groupby(by="review_score")['review_id'].nunique().reset_index()
    review_df.rename(columns={
        "review_id": "review_count"
    }, inplace=True)
    return review_df

def create_customerplace_df(df):
    customerplace_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    customerplace_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    return customerplace_df

def create_sellerplace_df(df):
    sellerplace_df = df.groupby(by="seller_state").seller_id.nunique().reset_index()
    sellerplace_df.rename(columns={
        "seller_id": "seller_count"
    }, inplace=True)
    return sellerplace_df

# Data yang diberikan
customer1 = pd.read_csv(r'https://raw.githubusercontent.com/hilmafadiya1806/ProjectData/main/Dashboard/customer1.csv')
seller1 = pd.read_csv(r'https://raw.githubusercontent.com/hilmafadiya1806/ProjectData/main/Dashboard/seller1.csv')
review2 = pd.read_csv(r'https://raw.githubusercontent.com/hilmafadiya1806/ProjectData/main/Dashboard/review2.csv')

# Membuat DataFrame dari fungsi yang diberikan
review_df = create_review_df(review2)
customerplace_df = create_customerplace_df(customer1)
sellerplace_df = create_sellerplace_df(seller1)

# Tampilkan layout menggunakan Streamlit
st.title('Olish Store Dashboard')

col1, col2, col3 = st.columns(3)

with col1:
    # Menampilkan metrik untuk review DataFrame
    most_frequent_score = review_df.loc[review_df['review_count'].idxmax(), 'review_score']
    st.metric("Total Review", value=review_df['review_count'].sum())
    st.metric("Most Frequent Review Score", value=most_frequent_score)

    # Menampilkan plot untuk review score
    st.subheader('Review Score')
    st.write("Tabel ini menunjukkan distribusi jumlah review berdasarkan skor review.")
    with st.expander("Show Plot"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='review_score', y='review_count', data=review_df, palette='muted')
        plt.xticks(rotation=45)
        st.pyplot(fig)

with col2:
    # Menampilkan metrik untuk customer place DataFrame
    st.metric("Total Customers", value=customerplace_df['customer_count'].sum())

    # Menampilkan plot untuk customer place DataFrame
    st.subheader('Customer Places')
    st.write("Tabel ini menunjukkan jumlah pelanggan dari setiap negara bagian.")
    with st.expander("Show Plot"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='customer_state', y='customer_count', data=customerplace_df, palette='viridis')
        plt.xticks(rotation=45)
        st.pyplot(fig)

with col3:
    # Menampilkan metrik untuk seller place DataFrame
    st.metric("Total Sellers", value=sellerplace_df['seller_count'].sum())

    # Menampilkan plot untuk seller place DataFrame
    st.subheader('Seller Places')
    st.write("Tabel ini menunjukkan jumlah penjual dari setiap negara bagian.")
    with st.expander("Show Plot"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='seller_state', y='seller_count', data=sellerplace_df, palette='mako')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Header untuk kesimpulan
st.header("Kesimpulan")
st.write("Dengan demikian dapat disimpulkan bahwa pelanggan sangat puas dengan pelayanan e-commerse. Disisi lain, daerah persebaran terbesar pelanggan maupun penjual pada daerah yang sama yaitu SP. Oleh karena itu, untuk meningkatkan kepuasan pelanggan kedepannya dapat dilakukan penyebaran daerah penjual agar daerah pelanggan juga lebih tersebar didaeran lain.")
