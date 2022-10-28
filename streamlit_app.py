import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('This is the header')
streamlit.text('This is text.')
streamlit.text('This is also text.\n 🥣 🥗 🐔 🥑🍞')
streamlit.text('Hey, more text.')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
