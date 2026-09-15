
import streamlit as st
import pickle

pickle_in = open('D:\CODING\IIT internship\merge.pkl','rb')
merge= pickle.load(pickle_in)

pickle_in = open(r'D:\CODING\IIT internship\f1.pkl','rb')
f1= pickle.load(pickle_in)

pickle_in = open('D:\CODING\IIT internship\data.pkl','rb')
data= pickle.load(pickle_in)

st.title("Stock Price Prediction using Sentimental Analysis")

st.sidebar.subheader("Generate the Combined dataset used to build the project")
if st.sidebar.button("Generate", key='1'):
    st.write("Here's your combined dataset:")
    st.write(merge)


st.sidebar.subheader("Generate the Subjectivity , Polarity and Sentiment scores of the news headlines ")
if st.sidebar.button("Generate", key='2'):
    st.write("Here's your data:")
    st.write(data)


st.sidebar.subheader("Generate the F1 Score of the Model's Prediction ")
if st.sidebar.button("Generate",key='3'):
    st.write("Here is the F1 Score of the ML model :")
    st.write(f1)
