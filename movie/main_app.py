import streamlit as st
from PIL import Image

# 画像を挿入
image = Image.open('./data/image.png')
st.image(image, width = 1000)


# タイトル
st.title('映画レコメンドシステム')

# キャプション
st.caption('これはあなたのコメントからおすすめの映画を紹介するシステムです')