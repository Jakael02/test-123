import streamlit 
import numpy as np
import streamlit as st
import pandas as pd

#Title must come pre-defined font size & type
streamlit.title('My Parents New Healthy Diner')

#Header
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


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


#Line Chart with Random Numbers
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Add a widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



