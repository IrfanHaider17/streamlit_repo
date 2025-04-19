import streamlit as st
import pandas as pd

st.title('Streamlit App')
"""'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
st.write(df)

code = '''
st.title('mytitle')
st.header("my header")
st.subheader('my subheader')
name = st.text_input('input your name: ')
age = st.number_input('input your age: ')

if st.button('submit'):
    if name and age:
        st.write('hello', name, 'your age is ', age)
    else:
        st.warning('please fill in all the fields')
'''
st.code(code, language='python')
st.selectbox('select your favoutite color', ['red', 'blue', 'green'])
st.slider('select your age', 0, 100)
df1 = pd.read_csv('titanic.csv')
st.line_chart(df1['Age'])
'''
"""
st.title("Simple Form")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1)
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")

st.markdown('this is markdown')
st.markdown('# this is markdown')
st.markdown('## this is markdown')
st.markdown('### this is markdown')
st.markdown('#### this is markdown')
st.markdown('##### this is markdown')