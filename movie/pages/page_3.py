import streamlit as st
import pandas as pd




# 参照はmain_app.pyからの相対参照
df = pd.read_csv('./movie/data/dairy_products.csv')
st.dataframe(df)