import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime as dt
from io import StringIO 
import time





st.set_page_config(page_title="منشورات وزاة الحج", page_icon=":bar_chart:",
                   layout="wide", )

col, col0 = st.columns(2)
with col0:
    
    
    st.markdown("<h4 style='text-align: right; color: black; margin-top:40px; font-family: 'Tajawal';'> حجاج الداخل </h4>",
                unsafe_allow_html=True)
    

with col:
    st.image('haj_logo.png', caption='وزارة الحج')


sheet_url3 ="https://docs.google.com/spreadsheets/d/1Q1CiTQleRVunDGLuwDW0pMhGBDZ0jxTZJUaPiyq3CG4/edit#gid=1595164542"
url_manshorat = sheet_url3.replace('/edit#gid=' , '/export?format=csv&gid=')



sheet_url4 ="https://docs.google.com/spreadsheets/d/193J0WI0iCyx_WwVgaSkDrKYw9xJlLKAZyRUv1-UXFeU/edit#gid=5850792"
url_manshorat_sent = sheet_url4.replace('/edit#gid=' , '/export?format=csv&gid=')






def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

@st.cache(allow_output_mutation=True)
def get_data():
    dataframe = pd.read_csv(url_manshorat)
    dataframe2 = pd.read_csv(url_manshorat_sent)
    # time.sleep(4)
    return dataframe , dataframe2
df, df_sentiment = get_data()

key_words_newspapers = ['mhmd alshykh', 'المصري اليوم', 'صحيفة سبق الإلكترونية',  'اليوم السابع', 'جريدة الرياض',
 'محمد الفايدي',
 'صلاح محمد',
 'cleverdes.com',
 'العربية.نت نادية الفواز',
 'الاسم *',
 'unknown',
 'Amabayzon stors',
 'Friday-',
 'babnet tunisie',
 'bwabt alakhbar',
 'nidal',
 'lebanon debate',
 'العربية السعودية',
 'واس الرياض',
 'altarykh',
 'الرياض الوطن',
 'المدينة المنورة علي العمري',
 'mzmz3',
 'الرياض',
 'الدمام',
 'أمل محمد',
 'صحيفة المدينة',
 'صحيفة',
 'wkalt alảnbaʾ alsʿwdyt',
 'صحيفة الوطن البحرينية',
 'wkalt alảnbaʾ alkwytyt',
 'aljzyrt ảwnlayn',
 'shyft sdy̱',
 'صحيفة المناطق',
 'مجلة سيدتي',
 'فتحي مجدي',
 'aboelfadl',
 'محمد تركي',
 'طارق حسنين',
 'مجلة سيدتي - sayidaty',
 'صحيفة صدى - مال واعمال',
 'alảrbʿaʾ m',
 'alảrbʿaʾ msaʾan',
 'alkhmys sbahaan',
 'althlathaʾ msaʾan',
 'alảrbʿaʾ sbahaan',
 'سارة السيد',
 'asmaa',
 'wkalt ảnbaʾ albhryn',
 '2018 , hqwq altbʿ walnshr bk50. kl alhqwq mhfwzt',
 'صحيفة البلاد',
 'الاقتصاد صحيفة',
 'ala̹qtsad shyft almdynt',
 'mal waʿmal shyft sdy̱',
 'sayidaty مجلة سيدتي',
 'khald alʿly',
 'علي احمد',
 'رضا النجار',
 'loovinsaudi',
 'mwso3h',
 'محمد السواح',
 'صحيفة الدستور',
 'alkhlyj aljdyd',
 'البوابه نيوز',
 'متابعات',
 'اب نيوز',
 'القدس العربي',
 'عدن لنج',
 'جريده المساء',
 '2022 كَشَّاف .',
 'محمد التهامي',
 'zhyr bn jmʿh alghzal',
 'mndhu',
 'alảrbʿaʾ',
 'alkhmys',
 'akhbar 24',
 'althlathaʾ',
 'mstfy̱ syd',
 'الاقتصادية (السعودية)',
 'كويت تايمز',
 'السيارات',
 'الجزيرة (السعودية)',
 'البلاد (السعودية)',
 'alnshrt (lbnan)',
 'المربع نت',
 'الوطن السعودية',
 'aqrả ảydaan',
 'البلاد',
 'عكاظ',
 'tm alnshr fy',
 'صحيفة غراس _ الرياض',
 'mfdy alkhmsany',
 'الاسم',
 'khald hamd',
 'جميع الحقوق محفوظة',
 'صحيفة غراس - الرياض',
 'علي العمري',
 'alkhmys s',
 'الوطن',
 'alkhrj',
 'صحيفة غراس - واس',
 'dimensions of information.',
 'الجوهرة',
 'صحيفة الاقتصادية',
 'brwfayl alryad',
 'فريق التحرير',
 'صحيفة عكاظ',
 'صحيفه واصل',
 'بوابة الفجر المصرية',
 'brwfayl was alryad',
 'brwfayl alryad -',
 'alwtn ny̰wz',
 'bizbahrain',
 'مملكة البحرين',
 'مريم الحويطي',
 'فاطمه العنزي',
 'العين اونلاين',
 'admin',
 'akhbar mhlyt',
 'hdrmwt 4 thwany',
 'عمان',
 'كريمة سعيد',
 'ảmryka',
 'صحيفة الرياض',
 'ảhmd ảbrahym',
 'جريدة الرياض',
 'اليمن',
 'صحيفة تواصل',
 'الجزيرة',
 'جريدة المدينة',
 'hdrmwt mndh thanyt',
 'العراق',
 'hdrmwt 6 thwany',
 'صحيفة صراحة الالكترونية',
 'صحيفة سبق',
 'mohamed nasa',
 'الوطن نيوز',
 'copyright ©',
 'لبنان',
 'rsha mhmd',
 'hdrmwt 38 thanyt',
 'تونس',
 'al anzi',
 'alshrwq mndh 53 dqyqt',
 '0 تعليقات',
 'عبدالله بورسيس',
 'alshrwq mndh 8 thanyt',
 'محمد يوسف',
 'shyft ala̹qtsadyt',
 'alshrwq mndh 5 thanyt',
 'عين الوطن',
 'ảkhbar alsʿwdyt',
 'حسين مصعود',
 'ala̹marat',
 'صـحـيـفـة الـجـزيـرة',
 'صحيفة البيان',
 'صحيفة الخليج',
 'صحيفة اليوم',
 'جريدة البداية',
 'صحيفة المناطق السعودية',
 'صحيفة جيل اليوم الالكترونية',
 'بلدنا',
 'alảhsaʾ',
 'alwkalt alʿrbyt alswryt llảnbaʾ',
 'ala̹khbaryt 24',
 'عدّاد جدة',
 'أخبار جهينة الرسمي',
 'نجران الان',
 '#عناوين_المدينة',
 'powerd by',
 'alảthnyn m',
 'akhbar akhbar thqfny',
 'نور عزت',
 'عدن الان',
 'ảʿmal',
 'خيال',
 'ashbalsajer',
 'fateenah',
 'alảthnyn',
 'Sakina Fatima',
 'جمعان الكناني',
 'bwabt ảkhbar',
 'صحيفة المقال',
 'المصري',
 'alathnyn sbahaan',
 'almghrb',
 'alảhd msaʾan',
 'فلسطين',
 'alảkhbar shyft sdy̱',
 'صحيفة صدى - الأخبار',
 'يوسف حسن مكة المكرمة',
 'علي الجابري',
 'shʿban twkl',
 'ahmd yhyy̱ mhmd aldysty',
 'المحليات صحيفة',
 'واس مكة المكرمة',
 '(السعودية)',
 'alảkhbar',
 'صراحة نيوز',
 'بوابة الاخبار',
 'ảkhbarna',
 'مصراوي',
 'مصراوي - أخبار مصر',
 'المحليات',
 'ảkhbark.nt',
 'alảhd m',
 'ala̹marat nywz',
 'وسام محمد',
 'الفجيرة نيوز',
 'عداد الزوار 51',
 '2:48 م',
 'ترند',
 'maryna bshart',
 'msdr shyft sbq ala̹lktrwnyt',
 'alathad (ala̹maratyt)',
 'afry̰qa ny̰wz',
 'hqwq alnshr 2022, jmyʿ alhqwq mhfwzt',
 'ahmad pharaoan',
 'مصدر صحيفة الاتحاد',
 'alrảy rsd',
 'مصدر صحيفة تواصل',
 'اطلس سكوب',
 'alsadq alʿthmany',
 'مصدر صحيفة البيان',
 'jrydt ala̹thad',
 'akhr thdyth',
 'الحقوق محفوظة النيلين 2022',
 'aldstwr (alảrdnyt)',
 'النهار (الكويتية)',
 'جاسم الهنداسي',
 'المصدر وكالات',
 'Hala Akhbar',
 'alảhd-',
 'مريم الجابري',
 'khbrk.net',
 'المصدر البيان',
 'سواليف',
 'dyna shʿyb',
 'ảna alkhbr',
 'البوابه قطر',
 'alảhd sbahaan',
 'البوابه تونس',
 'Fahad Al-Slmani',
 'alsbt msaʾan',
 'الرياضية',
 'Editor',
 'الجمعة م',
 'صحيفة المجاردة',
 'اخبار ثقفني - اخبار اليوم',
 'صنعاء نيوز',
 'امير السيد',
 'alshrwq mndh 12 thanyt',
 'aljmʿt sbahaan',
 'nasrine o.',
 'مصدر صحيفة الوئام',
 'المدينة (السعودية) الجمعة',
 'المدينة جدة',
 'العربية بيزنس',
 'مارب',
 'الجمعة ص',
 'احمد رفعت',
 'ảhmd slah',
 'الرياض الجمعة',
 'مصدر جريدة الوطن السعودية',
 'ảkhbar msr',
 'محمد شطا',
 'mshahdt qnat am by sy msr bth mbashr mbc masr live',
 'Mohamed Omran',
 'مصدر صحيفة عاجل',
 'صحيفة المناطق - محليات',
 '«عكاظ» (جدة) okaz_online@',
 'السبت م',
 'bwabt alshrwq',
 'rsha mhdy',
 'صراحة',
 'مكة المكرمة :الوطن',
 'وطن نيوز',
 'alʿrbyt nt hamd alqrshy',
 'mstfy̱ ảbw adm',
 'وکاله رسا',
 'محمد جمال',
 'جريدة الديار',
 'bwabt alảsbwʿ',
 'mohamed',
 'بوابة الدولة',
 'shfqna alʿraq',
 'almshhd alymny',
 'akhbarna',
 'جريدة الموجز',
 'ElKhabar',
 'موقع السلطة',
 'nhy ảhmd',
 'النهار مصر',
 'محمد رجب السنهوري',
 'ymn fywtshr',
 'wkalt khbr',
 'ayman ảhmd',
 'الكاتب',
 'ảnbaʾ almsryt',
 'الوظيفة مروك.كوم',
 'copyright â islamtimes.org 2022 , all rights reserved',
 'السومرية نيوز',
 'ảsmaʾ hsny̱',
 'Unknown',
 'سبوتنيك عربي',
 'Alsumaria Tv',
 'مصدر صحيفة الاقتصادية',
 'alkhbr alymny',
 'السومرية الفضائية العراقية',
 'المدينة متابعات',
 'alwfd alsbt',
 'a̹kram ʿbd alʿzyz',
 'sraht alsbt',
 'shyft ʿajl ala̹lktrwnyt',
 'shyft almwatn ala̹lktrwnyt',
 'تواصل',
 'syast alkhswsyt',
 'اسلام جمال',
 'ảkhbar aqtsadyt shyft alaqtsadyt',
 'ʿkaz alsbt',
 'تصميم مجلة الووردبريس',
 '«عكاظ» (جدة)',
 '«الاقتصادية» من الرياض',
 'سبق',
 'جريدة النهار',
 'minute',
 'sbahaan',
 'sydty alảhd',
 'elaosboa.com',
 'alảkhbar almsayy̱',
 'الرياض/سما/',
 'Abdulhakim Zaqoot',
 'alsbt btwqyt ghryntsh',
 'shyft alnkhbt',
 'alkhmys m',
 'hdrmwt mndh dqyqt',
 'alshrq alảwst 41 dqyqt',
 'روسيا',
 'aljzyrt mbashr',
 'فزاع آل هلال',
 'البورصة',
 'حسن عبد الرحمن',
 'minutes',
 'اسماعيل الماحي',
 'رحمة',
 'alkhmys, s',
 'السابع',
 'jrydt alảnbaʾ alkwytyt',
 'عايدة قاسم',
 'Moviesle 00',
 '12:08 AM',
 'الرئيسية اتصل بنا',
 'alathnyn msaʾan',
 'صحيفة عاجل',
 'log in',
 'thmyl lʿbt hrb alkhlyj',
 'الوفد',
 'فاطمة المالكي',
 ]

key_words_gov = ['إدارة تعليم الرياض','وزارة الحج والعمرة', 'أبشر'
 'إدارة تعليم القصيم',
 'إدارة تعليم نجران',
 'إدارة تعليم الحدود الشمالية',
 'مركز الملك سلمان الاجتماعي',
 'إمارة منطقة الجوف',
 'جائزة الأميرة صيتة',
 'مدارس التربية النموذجية',
 'مجلس شباب حائل',
 'مكتب تعليم العارض',
 'مكتب تعليم الروضة',
 'مكتب تعليم قرطبة',
 'مكتب تعليم الشفا',
 'مكتب تعليم الملز',
 'مكتب التعليم غرب المدينة المنورة - بنين',
 'مدرسة عامر بن ربيعة',
 'وزارة الصحة السعودية',
 'وزارة الداخلية',
 'وزارة التعليم - عام',
 'الجوازات السعودية',
 'المرور السعودي',
 'أمانة محافظة جدة',
 'الأحوال المدنية',
 'الأمن العام',
 'الخارجية الأمريكية',
 'هيئة الغذاء والدواء',
 'الدفاع المدني السعودي',
 'وزارة السياحة',
 'وزارة البيئة والمياه والزراعة',
 'رئاسة شؤون الحرمين',
 '911',
 'وزارة الحج والعمرة',
 'إدارة تعليم جدة',
 'هيئة حقوق الإنسان',
 'مكافحة المخدرات',
 'الهيئة السعودية للتخصصات الصحية',
 'وزارة التربية والتعليم',
 'جامعة أم القرى',
 'أمانة المنطقة الشرقية',
 'جامعة الأميرة نورة',
 'وِزَارَةُ التَّرْبِيَةِ والتَّعْلِيم الأردنيَّة',
 'SDAIA',
 'صندوق التنمية العقارية',
 'التدريب التقني',
 'وزارة النقل والاتصالات وتقنية المعلومات',
 'عمادة شؤون الطلاب',
 'جامعة القصيم',
 'جامعة الإمام عبدالرحمن بن فيصل',
 'الهيئة العامة للإحصاء',
 'وكالة شؤون المسجد النبوي',
 'جامعة حائل',
 'أمانة منطقة المدينة المنورة',
 'جامعة تبوك',
 'برنامج التحول الوطني',
 'وزارة الموارد البشرية والتنمية الاجتماعية',
 'أبشر',
 'وزارة العدل',
 'التأمينات الاجتماعية',
 'وزارة الشؤون البلدية والقروية والإسكان',
 'وزارة النقل والخدمات اللوجستية',
 'المواصفات السعودية',
 'منشآت',
 'جامعة الملك سعود',
 'وزارة الاتصالات وتقنية المعلومات',
 'وزارة الطاقة',
 'هيئة تقويم التعليم والتدريب',
 'جامعة طيبة Taibah U',
 'مدينة الملك عبدالعزيز للعلوم والتقنية',
 'إمارة منطقة عسير',
 'مجلس الضمان الصحي',
 'مدينة الملك فهد الطبية',
 'الهيئة الملكية لمحافظة العلا',
 'مستشفى الملك فيصل التخصصي ومركز الأبحاث',
 'وزارة الصناعة والثروة المعدنية',
 'هيئة المحتوى المحلي والمشتريات الحكومية',
 'إدارة تعليم المدينة المنورة',
 'مجلس التعاون',
 'جـامعة شقراء',
 'صحة الـشرقية',
 'صـحــة الـريــاض',
 'صـحة جدة',
 'أمانة منطقة تبوك',
 'إمارة منطقة تبوك',
 'آمــر',
 'صحـــة جــازان',
 'إدارة تعليم جازان',
 'إمارة منطقة حائل',
 'هيئة رعاية الأشخاص ذوي الإعاقة',
 'هيئة الحكومة الرقمية',
 'إدارة تعليم محايل عسير',
 'صحة تبوك',
 'صحة حفر الباطن',
 'الإدارة العامة للشراكة المجتمعية',
 'إدارة تعليم الزلفي',
 'جامعة جازان',
 'جمعية الثقافة والفنون',
 'جمعية حركية ♿']
key_words_channels = [ 'شبكة المجد'
 ,'إذاعة الرياض',
'صباح السعودية🇸🇦', 'قناة MBC'
,
'روتانا خليجية','mbc', 'RT online', 'شمس FM', 'CNN Indonesia', 'قناة المملكة' , 'قناة الجزيرة' , 'إذاعة جدة' , 'ميديا وان تي في' , 'أخبار قناة السعودية' , 'رادیو بین المللی عربستان سعودی_ بخش فارسی' , 'اتحاد اذاعات وتليفزيونات دول منظمةالتعاون الإسلامي' , 'إذاعة ألف ألف', 'قناة اقرأ الفضائية', 'روتانا خليجية', 'العربية السعودية' , 'جدة الان | JeddahNow', 'قناة الرسالة', 'برنامج سيدتي' , '#برنامج_أخباركم']

@st.cache(allow_output_mutation=True)
def get_newspapers (df, key_words):
    # with st.spinner(' جاري تحضير التقرير! انتطر من فضلك...'):

               
    newlist = pd.Series()

    for key in key_words:
            news = df['extra_author_attributes.name'].str.contains(key) 

            
            newlist = newlist.append(news)
        
        

    newestlist  = newlist.to_frame()
    news_paper = newestlist[newestlist[0] == True]

    news_paper  = news_paper.sort_index()

    

    news_paper_results = pd.merge(df, news_paper, left_index=True, right_index=True)

    news_paper_results1 = news_paper_results.sort_values(by= ['reach'], ascending=False)
                

    return news_paper_results1

df_news_papers = get_newspapers(df, key_words_newspapers)




df_gov = get_newspapers(df, key_words_gov)

df_channels = get_newspapers(df, key_words_channels)






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
                dts = st.date_input(label='Date Range: ', value=(dt(year=2022, month=9, day=10, hour=16, minute=30), 
                dt(year=2023, month=2, day=21, hour=16, minute=30)),
                key='#date_range',
                help="The start and end date time")
                
                st.write('Start: ', dts[0], "End: ", dts[1])
            
            

               

            except:
                st.write("You must pick a start and end date")
                st.stop()
                
            df_dated = df[(df["indexed"] <=  '{}'.format(dts[1])) & (df['indexed'] >=  '{}'.format(dts[0]))] 
            df_sentiment_dated = df_sentiment[(df_sentiment["Date"] <=  '{}'.format(dts[1])) & (df_sentiment['Date'] >=  '{}'.format(dts[0])) ] 
            df_newspapers_dated = df_news_papers[(df_news_papers["indexed"] <=  '{}'.format(dts[1])) & (df_news_papers['indexed'] >=  '{}'.format(dts[0]))] 
            df_gov_dated = df_gov[(df_gov["indexed"] <=  '{}'.format(dts[1])) & (df_gov['indexed'] >=  '{}'.format(dts[0]))] 
            df_channels_dated = df_channels[(df_channels["indexed"] <=  '{}'.format(dts[1])) & (df_channels['indexed'] >=  '{}'.format(dts[0]))] 

          
            
            
            



 
col1, col2, col3 = st.columns(3)
with col1:
    with st.container():
       
        st.markdown("<h6 style='text-align: center; color: black; '>إجمالي المنشورات</h6>", unsafe_allow_html=True)
        try:
            total_posts = len(df_dated. index)
            st.markdown("<h4 style='text-align: center; color: black;'>{}</h4>".format(total_posts), unsafe_allow_html=True)
        except:
            st.write('حمل البيانات')





    

with col2:
    st.markdown("<h6 style='text-align: center; color: black;'>معدل تكرار الوصول</h6>", unsafe_allow_html=True)
    try:
        reach = round(df_dated['reach'].sum()/1000000, 1) 
        st.markdown("<h4 style='text-align: center; color: black;'><h7 style='text-align: center; color: black;'> مليون </h7>{}        </h4>".format(reach), unsafe_allow_html=True)
    except:
        st.write('حمل البينات أولا')

with col3:
    st.markdown("<h6 style='text-align: center; color: black;'>معدل التفاعل</h6>", unsafe_allow_html=True)
    try:
        engagement = round(df_dated['engagement'].sum())
        st.markdown("<h4 style='text-align: center; color: black;'>{}</h4>".format(engagement), unsafe_allow_html=True)
    except:
        st.write('حمل البينات أولا')


col4, col5 = st.columns([1,1.4])


with col4:

    try:
        positive = df_sentiment_dated['Positive'].sum()
        negative = df_sentiment_dated['Negative'].sum()
        neutral = df_sentiment_dated['Neutral'].sum()
        all_sentiment = positive + negative + neutral
    

        pos_percent = round((positive/all_sentiment) *100, 1)
        neg_percent = round((negative/all_sentiment) *100, 1)
        neut_percent = round((neutral/all_sentiment) *100, 1)
        perecent_sent = [pos_percent, neut_percent, neg_percent]
        names =['positive', 'neutral', 'negative']
    
        fig_sentiment = px.pie(  values= perecent_sent, names=names,color= ['positive', 'neutral', 'negative'] , color_discrete_map={'positive': '#186e06', 'neutral': '#f9e106', 'negative': '#e2060a'}, 
            title="نبرة التفاعل",)
        fig_sentiment.update_layout({"plot_bgcolor": "rgba(0, 0, 0, 0)",  "paper_bgcolor": "rgba(0, 0, 0, 0)",}, margin=dict(l=50, r=100, t=50, b=50),)

        graph = st.plotly_chart(fig_sentiment, use_container_width = True)
    except:
        st.write('حمل البينات أولا')

        


with col5:

    try:
        
        df_countries = df_dated['extra_article_attributes.world_data.country'].value_counts().to_frame().head(10)
        df_countries['الدولة'] = df_countries.index
        


    
        fig_countries = px.pie(df_countries, color = 'الدولة',values=df_countries['extra_article_attributes.world_data.country'], names=df_countries['الدولة'],  title="الدول", labels={
                               'extra_article_attributes.world_data.country': 'المشاركات'})
        fig_countries.update_layout({"plot_bgcolor": "rgba(0, 0, 0, 0)" ,  "paper_bgcolor": "rgba(0, 0, 0, 0)", }, margin=dict(l=50, r=50, t=50, b=50),)
       
        st.plotly_chart(fig_countries, use_container_width = True)
    except:
        st.write('حمل البينات أولا')

            

        
    








bottom_container = st.container()
col6, col7, col8, col9  = st.columns(4)
with bottom_container:
    st.markdown("<h6 style='text-align: right; color: black;'>مواضيع الرصد</h6>", unsafe_allow_html=True)

    with col6:
        
        st.markdown("<h6 style='text-align: center; color: black;'>حسابات تويتر أكثر من 50000 متابع</h6>", unsafe_allow_html=True)
        try:
            famous_df = pd.concat([df_dated, df_newspapers_dated, df_gov_dated, df_channels_dated, ]  ).drop_duplicates(keep=False, ignore_index=False)
            social_media_df = df_dated[(df_dated.host_url == 'http://twitter.com/' ) ]
            
            social_media_df = social_media_df [social_media_df.reach > 50000].sort_values(by= 'reach', ascending= False)
            social_media_df_dated = social_media_df[(social_media_df["indexed"] <=  '{}'.format(dts[1])) & (social_media_df['indexed'] >=  '{}'.format(dts[0]))]

            famous_df_final = social_media_df_dated[['url', 'indexed' , 'content_snippet', 'extra_source_attributes.name', 'extra_author_attributes.world_data.country' , 'reach' , 'engagement',]]
            famous_df_final = famous_df_final.rename({'url': 'الرابط' , 'indexed' : 'التاريخ', 'content_snippet' : 'الخير' , 'extra_source_attributes.name' : 'اسم الجريدة' , 'extra_author_attributes.world_data.country' : 'البلد' , 'reach' : 'معدل الوصول' , 'engagement' :'التفاعل'}, axis= 'columns')
            famous_df_final = famous_df_final.reset_index().drop(columns=['index'])
            famous_df_final1 = famous_df_final.to_csv().encode('utf-8-sig')
            st.markdown("<h3 style='text-align: center; color: black;'>{}</h3>".format(len(famous_df_final.index)),
            unsafe_allow_html=True)
            st.download_button(label= '  {}-{} اضغط لتحميل التقرير   '.format(dts[0], dts[1]), data=famous_df_final1, file_name='المشاهير  {} - {}.csv'.format(dts[0], dts[1]),
            mime='text/csv', )

        except:
            st.write('حمل البينات أولا')
    with col7:
            st.markdown("<h6 style='text-align: center; color: black;'>الصحف</h6>",
                unsafe_allow_html=True)
            


            
                    
            news_paper_results2 = df_newspapers_dated[['url', 'indexed' , 'content_snippet', 'extra_source_attributes.name', 'extra_author_attributes.world_data.country' , 'reach' , 'engagement',]]
            news_paper_results2 = news_paper_results2.rename({'url': 'الرابط' , 'indexed' : 'التاريخ', 'content_snippet' : 'الخير' , 'extra_source_attributes.name' : 'اسم الجريدة' , 'extra_author_attributes.world_data.country' : 'البلد' , 'reach' : 'معدل الوصول' , 'engagement' :'التفاعل'}, axis= 'columns')
            news_paper_results2 = news_paper_results2.reset_index().drop(columns=['index'])
            news_paper_results3 = news_paper_results2.to_csv().encode('utf-8-sig')
            st.markdown("<h3 style='text-align: center; color: black;'>{}</h3>".format(len(news_paper_results2.index)),
            unsafe_allow_html=True)
            st.download_button(label= '  {}-{} اضغط لتحميل التقرير   '.format(dts[0], dts[1]), data=news_paper_results3, file_name='الصحف  {} - {}.csv'.format(dts[0], dts[1]),
            mime='text/csv', )
            

                    

            


    with col8:
        st.markdown("<h6 style='text-align: center; color: black;'>الجهات الحكومية</h6>", unsafe_allow_html=True)

        gov_results2 = df_gov_dated[['url', 'indexed' , 'content_snippet', 'extra_source_attributes.name', 'extra_author_attributes.world_data.country' , 'reach' , 'engagement',]]
        gov_results2 = gov_results2.rename({'url': 'الرابط' , 'indexed' : 'التاريخ', 'content_snippet' : 'الخبر' , 'extra_source_attributes.name' : 'اسم الحساب' , 'extra_author_attributes.world_data.country' : 'البلد' , 'reach' : 'معدل الوصول' , 'engagement' :'التفاعل'}, axis= 'columns')
        gov_results2 = gov_results2.reset_index().drop(columns=['index'])
        gov_results3 = gov_results2.to_csv().encode('utf-8-sig')
        st.markdown("<h3 style='text-align: center; color: black;'>{}</h3>".format(len(gov_results2.index)),
        unsafe_allow_html=True)
        st.download_button(label= '  {}-{} اضغط لتحميل التقرير   '.format(dts[0], dts[1]), data=gov_results3, file_name='الجهات الحكومية  {} - {}.csv'.format(dts[0], dts[1]),
        mime='text/csv', )

    with col9:

        st.markdown("<h6 style='text-align: center; color: black;'> القنوات و الراديو</h6>", unsafe_allow_html=True)

        channels_results2 = df_channels_dated[['url', 'indexed' , 'content_snippet', 'extra_source_attributes.name', 'extra_author_attributes.world_data.country' , 'reach' , 'engagement',]]
        channels_results2 = channels_results2.rename({'url': 'الرابط' , 'indexed' : 'التاريخ', 'content_snippet' : 'الخبر' , 'extra_source_attributes.name' : 'اسم القناة' , 'extra_author_attributes.world_data.country' : 'البلد' , 'reach' : 'معدل الوصول' , 'engagement' :'التفاعل'}, axis= 'columns')
        channels_results2 = channels_results2.reset_index().drop(columns=['index'])
        channels_results3 = channels_results2.to_csv().encode('utf-8-sig')
        st.markdown("<h3 style='text-align: center; color: black;'>{}</h3>".format(len(channels_results2.index)),
        unsafe_allow_html=True)
        
        st.download_button(label= '  {}-{} اضغط لتحميل التقرير   '.format(dts[0], dts[1]), data=channels_results3, file_name='القنوات   {} - {}.csv'.format(dts[0], dts[1]),
        mime='text/csv', )

        





reports1 =st.expander('تفارير التفاعل من 7 سبتمبر - 7 أكتوبر')

with reports1:  
    
        
        
            

                url1 = 'https://drive.google.com/file/d/1F926hDpvx-6Js2anA_hznGeLc-7U4wmY/view?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 7 سبتبمر- 13 سبتمبر', ):
                    st.markdown(url1, unsafe_allow_html=True)

               
                    
                    
                    
                   
                   
                url2 ='https://docs.google.com/presentation/d/1MRit3bsPbDe6YPseAUZUVWb1zLrz8f5DlsWQO3iTpWo/edit?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 14 سبتبمر- 20 سبتبمر' ):
                    st.markdown(url2, unsafe_allow_html=True)
                

                url3 ='https://docs.google.com/presentation/d/1UiLNQF_N4UL2VqOSmG6tshILPY-rrHmTytIBdt4emNs/edit?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 21 سبتبمر- 27 سبتبمر' ):
                    st.markdown(url3, unsafe_allow_html=True)
        
        

                url4 ='https://docs.google.com/presentation/d/1pSZ73vLGYjJIZfd50FeHTaVq2sVuIRAMVHmHNpWUrNg/edit?usp=sharing'
                if st.button('رصد وزارة الحج والعمرة - 28 سبتبمر- 7 أكتوبر ' ):
                    st.markdown(url4, unsafe_allow_html=True)
reports2 =st.expander('تفارير التفاعل من 8 أكتوبر - 4 نوفمبر')
with reports2:
    url5 ='https://docs.google.com/presentation/d/1fgpkL4nog4h53bqnrHlFHtOiuLEPHz9Vt0RQJIIue-U/edit?usp=sharing'
    if st.button('رصد وزارة الحج والعمرة - 8 أكتوبر - 14 أكتوبر ' ):
        st.markdown(url5, unsafe_allow_html=True)

    url6 ='https://docs.google.com/presentation/d/1sWrFXucMRPgqYoxaycRVkOBAF9y-Kkl-Gjr1Q9fsDwU/edit?usp=sharing'
    if st.button('رصد وزارة الحج والعمرة - 15 اكتوبر -  21 أكتوبر' ):
        st.markdown(url6, unsafe_allow_html=True)
    url7 ='https://docs.google.com/presentation/d/1sWrFXucMRPgqYoxaycRVkOBAF9y-Kkl-Gjr1Q9fsDwU/edit?usp=sharing'
    if st.button('رصد وزارة الحج والعمرة - 22 اكتوبر -  28 أكتوبر' ):
        st.markdown(url7, unsafe_allow_html=True)

    url8 ='https://docs.google.com/presentation/d/1ATxxi8GwKUMqDiBFgMcIqbhYG-JbelP1EQDuC0643ow/edit?usp=share_link'
    if st.button('رصد وزارة الحج 29 أكتوبر - 4 نوفمبر' ):
        st.markdown(url8, unsafe_allow_html=True)

reports3 =st.expander('تفارير التفاعل من 5 نوفمبر - 2 ديسمبر')
with reports3:
    url9 ='https://docs.google.com/presentation/d/1-V3pVGmMhcmliZ2sG_mgoekS4f2SkzRRzu3oRe9LGzs/edit?usp=share_link'
    if st.button('رصد وزارة الحج والعمرة 5 نوفمبر - 11 نوفمبر ' ):
        st.markdown(url9, unsafe_allow_html=True)

    url10 ='https://docs.google.com/presentation/d/1fXesKkF8NqnCwUTOC2iAqHnHfQZh9cWfF_e8VuoPvw4/edit?usp=share_link'
    if st.button('رصد وزارة الحج 12 نوفمبر - 18 نوفمبر' ):
        st.markdown(url10, unsafe_allow_html=True)
    url11 ='https://docs.google.com/presentation/d/1_iURDzUrsJ0FMeaGDlM_edpVTZooi6ori0w9rUwfIhk/edit?usp=share_link'
    if st.button('رصد وزارة الحج 19 نوفمبر - 25 نوفمبر' ):
        st.markdown(url11, unsafe_allow_html=True)

    url12 ='https://docs.google.com/presentation/d/11mcdWHj_xm3aLSaHd8rfdS2TQ-1w1kp68Lu8KJu4ky4/edit?usp=share_link'
    if st.button('رصد وزارة الحج 26 نوفمبر - 2 ديسمبر' ):
        st.markdown(url12, unsafe_allow_html=True)

reports4 =st.expander('تفارير التفاعل من 3 ديسمبر - 30 ديسمبر ')
with reports4:
    url13 ='https://docs.google.com/presentation/d/1bdJUx-wRnxqGiwt4AS0s-9qJ-rLpIV97fiUfFB7syto/edit?usp=share_link'
    if st.button('رصد وزارة الحج 3 ديسمبر- 9 ديسمبر' ):
        st.markdown(url13, unsafe_allow_html=True)

    url14 ='https://docs.google.com/presentation/d/1rTtfy0ZoVQUnnvO6btAdwV-25Ax2qCK44MayIkSDMCc/edit?usp=share_link'
    if st.button('رصد وزارة الحج 10  ديسمبر- 16 ديسمبر' ):
        st.markdown(url14, unsafe_allow_html=True)
    url15 ='https://docs.google.com/presentation/d/1AqBKp4V3dU8TTAtPOYPM-AYdJSjGoWEWY7GScIFVWNk/edit?usp=share_link'
    if st.button('رصد وزارة الحج 17  ديسمبر- 23 ديسمبر' ):
        st.markdown(url15, unsafe_allow_html=True)

    url16 ='https://docs.google.com/presentation/d/1q3eux1CxyyyqB0PNlPzXFX-DELclah0Fdc05_ETpRDs/edit?usp=share_link'
    if st.button('رصد وزارة الحج 24  ديسمبر-30  ديسمبر'):
        st.markdown(url16, unsafe_allow_html=True)
    
            


            





hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)









