import streamlit as st
import pandas as pd




# 参照はmain_app.pyからの相対参照
df = pd.read_csv('../data/dairy_products.csv')
st.dataframe(df)