import streamlit as st


# サブヘッダー
st.subheader('好みの映画を探すのは難しいですよね、、、')

# テキスト
st.text('あなたのコメントと似ているコメントを探し高評価の映画を紹介する仕様になっています')
st.text('制度に関してはノーコメントでお願いします')


# コードの挿入
code = '''
import streamlit as st

st.title('映画レコメンドシステム')
'''

st.code(code, language = 'python')
