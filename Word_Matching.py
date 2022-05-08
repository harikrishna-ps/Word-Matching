
import streamlit as st 
from fuzzywuzzy import fuzz


st.title('Word Matching')

Str1 = st.text_input("Enter the First Word Here...")
Str2 = st.text_input("Enter the Second Word Here...")
if st.button('Get Results'):
    Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
    st.write("The Matching Ratio is ")
    st.subheader(Ratio)

