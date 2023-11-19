import streamlit 
import numpy as np
import streamlit as st
import pandas as pd
import json
from snowflake.snowpark import Session

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈✅ :anchor:")

#Title must come pre-defined font size & type
streamlit.title('My Parents New Healthy Diner')

#Header
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

file = st.file_uploader(
    "Drop your CSV here to load to Snowflake",type={"csv"})



#My first "Data Frame" with made up numbers
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

df


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

#Line Chart with Random Numbers
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Add a widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



