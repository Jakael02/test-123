import streamlit as st
from streamlit.logger import get_logger

#LOGGER = get_logger(__name__)


#def run():
#   st.set_page_config(
#       page_title="Hello",
#       page_icon="👋",
#   )

#    st.write("# Welcome to Streamlit 2.0!! 👋")

#    st.sidebar.success("Select a demo above.")

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

if __name__ == "__main__":
    run()
