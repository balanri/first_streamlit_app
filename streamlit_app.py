import streamlit
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text  ('π₯£Omega 3 & Blueberry oatmeal')
streamlit.text  ('π₯ Kale , Spinach & Rocket Smoothie')
streamlit.text  ('πHard-Boiled Free-Range Egg')
streamlit.text( ' π₯π Avocado Toast')
 
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')
import pandas 
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
