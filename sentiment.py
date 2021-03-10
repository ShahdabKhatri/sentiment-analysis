import streamlit as st
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.title('This is sentiment analysis app')
st.markdown('### Enter your text ')
txt = st.text_area('.','Shahdab is the creator of this App')
sen=SentimentIntensityAnalyzer()
if st.button('submit'):
    st.success('submitted')
dic=sen.polarity_scores(txt)
polarity=None
if dic['neg']>0.2:
    polarity= -1
elif dic['pos']>0.2:
    polarity = 1
else: 
    polarity =0
if polarity ==1 :
    st.write('Its positive')
    img=Image.open(r'smile.png')
    st.image(img)

elif polarity ==-1:
    st.write('Its negative')
    img=Image.open(r'angry.png')
    st.image(img)

else:
    st.write('Its neutral')
    img=Image.open(r'neutral.png')
    st.image(img)
