import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime as dt
from io import StringIO 
import time
import webbrowser

st.set_page_config(page_title="منشورات وزاة الحج", page_icon=":bar_chart:",
                   layout="wide", initial_sidebar_state='collapsed')
col, col0 = st.columns(2)
with col0:

    st.markdown("<h4 style='text-align: right; color: black; margin-top:40px;'>منصة مقام</h4>",
                unsafe_allow_html=True)

with col:
    st.image('haj_logo.png', caption='وزارة الحج')


sheet_url3= 'https://docs.google.com/spreadsheets/d/1YUo1kcoaDjPI9FiyOYS9YriIZbnF9at8F0dhDRwtd3M/edit#gid=1379378486'
url_manshorat_maqam = sheet_url3.replace('/edit#gid=' , '/export?format=csv&gid=')

sheet_url4= 'https://docs.google.com/spreadsheets/d/1pxKv8U8uU3QK4wzGaSftevkR1Oyw2iDAHnlKeFoJVso/edit#gid=352640152'
url_maqam_sent = sheet_url4.replace('/edit#gid=' , '/export?format=csv&gid=')




def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

@st.cache(allow_output_mutation=True)
def get_data1():
    dataframe = pd.read_csv(url_manshorat_maqam)
    dataframe2 = pd.read_csv(url_maqam_sent)
    # time.sleep(4)
    return dataframe , dataframe2
df, df_sentiment = get_data1()





with st.sidebar:
    
    
            st.markdown("<div style= 'background-image: {}; display: block; margin-left: auto;  margin-right: auto;' ></div>".format(
                st.image('intrend_logo.png', caption='Intrend إليكم من')), unsafe_allow_html=True)
            
            
            date2 = pd.to_datetime(df["indexed"]).dt.strftime('%Y-%m-%d')
            df['indexed'] = date2

           
            date = pd.to_datetime(df_sentiment.Date)
            df_sentiment['Date'] = date

            
            if len(df_sentiment.columns )== 3:
                df_sentiment['Date'] = date
                
                
                df_sentiment['Negative'] = 0
            else:
                df_sentiment = df_sentiment
                df_sentiment['Date'] = date
            

            

           


            try:
                dts = st.date_input(label='Date Range: ', value=(dt(year=2022, month=9, day=29, hour=16, minute=30), 
                dt(year=2022, month=12, day=29, hour=16, minute=30)),
                key='#date_range',
                help="The start and end date time")
                st.write('Start: ', dts[0], "End: ", dts[1])
            
            
                df_dated = df[(df["indexed"] <=  '{}'.format(dts[1])) & (df['indexed'] >=  '{}'.format(dts[0]))] 

                df_sentiment_dated = df_sentiment[(df_sentiment["Date"] <=  '{}'.format(dts[1])) & (df_sentiment['Date'] >=  '{}'.format(dts[0])) ] 
            except:
                st.write("You must pick a start and end date")
                st.stop()
            
            
            
            



 
col1, col2, col3 = st.columns(3)
with col1:
    with st.container():
       
        st.markdown("<h6 style='text-align: right; color: black;'>إجمالي المنشورات</h6>", unsafe_allow_html=True)
        try:
            total_posts = len(df_dated. index)
            st.markdown("<h4 style='text-align: right; color: black;'>{}</h4>".format(total_posts), unsafe_allow_html=True)
        except:
            st.write('البيانات غير متاحة')





    

with col2:
    st.markdown("<h6 style='text-align: right; color: black;'>معدل تكرار الوصول</h6>", unsafe_allow_html=True)
    try:
        reach = round(df_dated['reach'].sum()/1000000, 1) 
        st.markdown("<h4 style='text-align: right; color: black;'><h7 style='text-align: right; color: black;'> مليون </h7>{}        </h4>".format(reach), unsafe_allow_html=True)
    except:
        st.write('البيانات غير متاحة')

with col3:
    st.markdown("<h6 style='text-align: right; color: black;'>معدل التفاعل</h6>", unsafe_allow_html=True)
    try:
        engagement = df_dated['engagement'].sum()
        st.markdown("<h4 style='text-align: right; color: black;'>{}</h4>".format(engagement), unsafe_allow_html=True)
    except:
        st.write('البيانات غير متاحة')


col4, col5 = st.columns(2)


with col4:

    try:
        positive = df_sentiment_dated['Positive'].sum()
        negative = df_sentiment_dated['Negative'].sum()
        neutral = df_sentiment_dated['Neutral'].sum()
        all_sentiment = positive + negative + neutral
    

        pos_percent = round((positive/all_sentiment) *100, 1)
        neg_percent = round((negative/all_sentiment) *100, 1)
        neut_percent = round((neutral/all_sentiment) *100, 1)
        fig_sentiment = px.bar( width= 500, x=[pos_percent, neut_percent, neg_percent], y=['positive', 'neutral', 'negative'],color= ['positive', 'neutral', 'negative'] , color_discrete_map={'positive': '#186e06', 'neutral': '#f9e106', 'negative': '#e2060a'}, 
            orientation='h', title="نبرة التفاعل", labels={'x': 'النسبة المئوية', 'y': ''}, text= ['{} %'.format(pos_percent), '{} %'.format(neut_percent), '{} %'.format(neg_percent)])
        fig_sentiment.update_yaxes(autorange="reversed")

        graph = st.plotly_chart(fig_sentiment)
    except:
        st.write('البيانات غير متاحة')

        


with col5:

    try:
        
        df_countries = df_dated['extra_article_attributes.world_data.country'].value_counts().to_frame().head(10)
        df_countries['الدولة'] = df_countries.index
        


    
        fig_countries = px.bar(df_countries, width=600, color = 'الدولة',x=df_countries['extra_article_attributes.world_data.country'], y=df_countries['الدولة'], orientation='h', title="الدول", labels={
                               'extra_article_attributes.world_data.country': 'المشاركات'})
        st.plotly_chart(fig_countries, )
    except:
        st.write('البيانات غير متاحة')

bottom_container = st.container()
col6, col7, col8  = st.columns(3)
with bottom_container:
    st.markdown("<h6 style='text-align: right; color: black;'>المنشورات</h6>", unsafe_allow_html=True)

    with col6:
        
        st.markdown("<h6 style='text-align: right; color: black;'>منشورات السوشيال ميديا</h6>", unsafe_allow_html=True)
        try:
            social_media = len(df_dated[df.host_url == 'http://twitter.com/'].index)
            st.markdown("<h4 style='text-align: right; color: black;'>{}</h4>".format(social_media), unsafe_allow_html=True)
        except:
            st.write('البيانات غير متاحة')
    with col7:
        st.markdown("<h6 style='text-align: right; color: black;'>الصحف</h6>", unsafe_allow_html=True)

        try:
            news_paper = len(df_dated[df.host_url != 'http://twitter.com/'].index)

            st.markdown("<h4 style='text-align: right; color: black;'>{}</h4>".format(news_paper), unsafe_allow_html=True)
        except:
            st.write('البيانات غير متاحة')
    with col8:
        st.markdown("<h6 style='text-align: right; color: black;'>أخرى</h6>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: right; color: black;'>0</h4>", unsafe_allow_html=True)
reports1 =st.expander('تفارير التفاعل من 7 سبتمبر - 7 أكتوبر')

with reports1:  
    
        
        
            

                url1 = 'https://drive.google.com/file/d/1F926hDpvx-6Js2anA_hznGeLc-7U4wmY/view?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 7 سبتبمر- 13 سبتمبر', ):
                    webbrowser.open(url1)
                    
                    
                    st.session_state.update(expanded = False)
                url2 ='https://docs.google.com/presentation/d/1MRit3bsPbDe6YPseAUZUVWb1zLrz8f5DlsWQO3iTpWo/edit?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 14 سبتبمر- 20 سبتبمر' ):
                    webbrowser.open(url2)
                

                url3 ='https://docs.google.com/presentation/d/1UiLNQF_N4UL2VqOSmG6tshILPY-rrHmTytIBdt4emNs/edit?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 21 سبتبمر- 27 سبتبمر' ):
                    webbrowser.open(url3)
        
        

                url4 ='https://docs.google.com/presentation/d/1pSZ73vLGYjJIZfd50FeHTaVq2sVuIRAMVHmHNpWUrNg/edit?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 28 سبتبمر- 7 أكتوبر ' ):
                    webbrowser.open(url4)
reports2 =st.expander('تفارير التفاعل من 8 أكتوبر - 4 نوفمبر')
with reports2:
    url5 ='https://docs.google.com/presentation/d/1fgpkL4nog4h53bqnrHlFHtOiuLEPHz9Vt0RQJIIue-U/edit?usp=sharing'
    if st.button('رصد وزارة الحج والعمرة - 8 أكتوبر - 14 أكتوبر ' ):
        webbrowser.open(url5)

    url6 ='https://docs.google.com/presentation/d/1sWrFXucMRPgqYoxaycRVkOBAF9y-Kkl-Gjr1Q9fsDwU/edit?usp=sharing'
    if st.button('رصد وزارة الحج والعمرة - 15 اكتوبر -  21 أكتوبر' ):
        webbrowser.open(url6)
    url7 ='https://docs.google.com/presentation/d/1sWrFXucMRPgqYoxaycRVkOBAF9y-Kkl-Gjr1Q9fsDwU/edit?usp=sharing'
    if st.button('رصد وزارة الحج والعمرة - 22 اكتوبر -  28 أكتوبر' ):
        webbrowser.open(url7)

    url8 ='https://docs.google.com/presentation/d/1ATxxi8GwKUMqDiBFgMcIqbhYG-JbelP1EQDuC0643ow/edit?usp=share_link'
    if st.button('رصد وزارة الحج 29 أكتوبر - 4 نوفمبر' ):
        webbrowser.open(url8)





hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)








