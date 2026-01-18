import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from bs4 import BeautifulSoup
import time

st.set_page_config(page_title="Amazon Analytics", layout="wide")

st.title("🛒 Amazon Sales Analytics Dashboard")
st.markdown("**Anamika Mishra | B.Tech CSE 2023 | Karnal**")

# Sample Amazon data (scraper will replace this)
sample_data = {
    'name': [
        'HP 15 i5 13th Gen', 'HP OmniBook OLED', 'Acer Aspire 3', 
        'ASUS Vivobook Go', 'Lenovo IdeaPad Slim', 'Dell Inspiron',
        'MacBook Air M2', 'Samsung Galaxy Book', 'MSI Modern 14'
    ],
    'price': ['₹55,990', '₹61,990', '₹25,990', '₹30,990', '₹45,990', 
              '₹52,990', '₹1,12,990', '₹68,990', '₹48,990']
}

df = pd.DataFrame(sample_data)
df['price_clean'] = df['price'].str.replace('₹', '').str.replace(',', '').astype(float)

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("📊 Total Products", len(df))
col2.metric("💰 Avg Price", f"₹{df['price_clean'].mean():.0f}")
col3.metric("🏆 Highest", f"₹{df['price_clean'].max():.0f}")
col4.metric("💎 Lowest", f"₹{df['price_clean'].min():.0f}")

# Charts
col1, col2 = st.columns(2)
with col1:
    fig = px.bar(df.sort_values('price_clean'), x='name', y='price_clean', 
                 title="Price Comparison")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.pie(df, names='name', values='price_clean', title="Price Share")
    st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df, use_container_width=True)
