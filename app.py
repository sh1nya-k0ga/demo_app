import streamlit as st
from PIL import Image
import datetime
import pandas as pd


dt = datetime.datetime.today()

# 同じディレクトリでstreamlit run app.py で走る

# 画像を挿入
image = Image.open('./data/image.png')
st.image(image, width = 1000)


# タイトル
st.title('映画レコメンドシステム')

# キャプション
st.caption('これはあなたのコメントからおすすめの映画を紹介するシステムです')


col1, col2 = st.columns(2)

with col1:
    # テキストボックス
    name  = st.text_input('名前')
    address = st.text_input('住所')
    
    
    # セレクトボックス
    # age_category = st.selectbox(
    #     '年齢層',
    #     ('---','子ども（18歳未満）','大人（18歳以上）'))
    
    # ラジオボタン
    age_category = st.radio(
        '年齢層',
        ('子ども（18歳未満）','大人（18歳以上）'))
    
    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング','アニメ','料理','釣り')
    )
    
    # チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    
    # スライダー
    height = st.slider('身長', min_value = 110, max_value = 210)
    
    # 日付
    start_date = st.date_input(
        '開始日',
        dt.date()
    )

    
    # ボタン
    submit_btn = st.button('送信')
    cancel_btn = st.button('キャンセル')


    if submit_btn:
        if (name == '') | (address == ''):
            st.error('名前または住所を入力してください。')
        else:
            st.text(f'ようこそ{name}さん！今日はどんな映画を見ましたか？')
            st.text(f'{address}に書籍を送りました')
            st.text(f'年齢層：{age_category}')
            st.text(f'趣味；{'、'.join(hobby)}')

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


# 画面をリロードすると入力が変数の中に入る
# ただ、デフォルトでは入力後のカーソルが外れるとリロードする仕様になっている



# 毎回リリードされるのはめんどくさい
# 次の方法で解決できる！

# with st.form(key = 'profile_form'):
    
#     # テキストボックス
#     name  = st.text_input('名前')
#     address = st.text_input('住所')
    
    
#     # セレクトボックス
#     # age_category = st.selectbox(
#     #     '年齢層',
#     #     ('---','子ども（18歳未満）','大人（18歳以上）'))
    
#     # ラジオボタン
#     age_category = st.radio(
#         '年齢層',
#         ('子ども（18歳未満）','大人（18歳以上）'))
    
#     # 複数選択
#     hobby = st.multiselect(
#         '趣味',
#         ('スポーツ','読書','プログラミング','アニメ','料理','釣り')
#     )
    
#     # チェックボックス
#     mail_subscribe = st.checkbox('メールマガジンを購読する')
    
#     # スライダー
#     height = st.slider('身長', min_value = 110, max_value = 210)
    
#     # 日付
#     start_date = st.date_input(
#         '開始日',
#         dt.date()
#     )

    
    
    

#     # ボタン
#     submit_btn = st.form_submit_button('送信')
#     cancel_btn = st.form_submit_button('キャンセル')


#     if submit_btn:
#         if (name == '') | (address == ''):
#             st.error('名前または住所を入力してください。')
#         else:
#             st.text(f'ようこそ{name}さん！今日はどんな映画を見ましたか？')
#             st.text(f'{address}に書籍を送りました')
#             st.text(f'年齢層：{age_category}')
#             st.text(f'趣味；{'、'.join(hobby)}')



with col2:
    
    df = pd.read_csv('./data/dairy_products.csv')
    st.dataframe(df)    # dfの挿入
#st.table(df)        # 固定でテーブルを表示する


# データの可視化編

# st.line_chart(df)
# st.bar_chart(df['2021年'])

# matplotlibも使える


# 画面分割

