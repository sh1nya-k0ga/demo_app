# 毎回リリードされるのはめんどくさい
# 次の方法で解決できる！

import streamlit as st

with st.form(key = 'profile_form'):
    
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
    # start_date = st.date_input(
    #     '開始日',
    #     dt.date()
    # )

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')


    if submit_btn:
        if (name == '') | (address == ''):
            st.error('名前または住所を入力してください。')
        else:
            st.text(f'ようこそ{name}さん！今日はどんな映画を見ましたか？')
            st.text(f'{address}に書籍を送りました')
            st.text(f'年齢層：{age_category}')
            st.text(f'趣味；{'、'.join(hobby)}')
