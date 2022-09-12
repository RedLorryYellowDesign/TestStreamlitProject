# ---| STEAMLIT APP STRUCTURE FILE |---

# See Cheetsheet here https://docs.streamlit.io/library/cheatsheet

# This app can be run locully by navigating to the directory and running.
# >>> streamlit run Your_Apps_Name.py
# Makesure you have all dependantsies installed locally first.

# installing dependantsies with pip from requirements.txt

# This app is desing test Streamlit
# and show how to use it. the structure
# of the app as well as the code and
# prerequisites. The app demonstrates
# how crete many components from applit

# ---| ALL IMPORT LIBRARIES |---
# Base Streamlit Libraries
import requests # Allows use of URL imports
import streamlit as st # Allows compatibility with Streamlit
from streamlit_lottie import st_lottie # Allows lottie animation
from PIL import Image # Image manipulation
# Data Science Libraries
import plotly as py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---| ELAMENTS SHOW ON WEBSITE |---
# The app is strcutured or rows and columns.
# >>> with st.container():
# we can create a container
# to group elements. The elements are then
# placed in the container. The container creates
# a row and the elements are placed in the row.
# Each row can be broke down into columns.
# >>> left_column, right_column = st.columns(2)
# This creates two columns in the row and
# each element is placed in the column by calling
# the column name and then indenting the element under it.

# Page configuraion
st.set_page_config(page_title="Test Streamlit App", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

# Use local css file to style the app
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# fucntion to load lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---| IMPORTING ASSEST |---
# Importing lottie animation
lottie_coding_Pyraminx_Shape_Lottie_Animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_2QAV9ZfHr4.json")
lottie_coding_Data_Science_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl3sktpc.json")

# Importing images

# Importing data
# df = pd.read_csv("CGP_data.csv")

# impoting Models from the models folder
# from models import model_name

# test DS Model with fake data and plot results
x = np.linspace(0, 20, 100)
fig = plt.figure()
plt.plot(x, np.sin(x))
plt.title('Matplotlib Graph', fontweight='bold')
plt.xlabel('x', fontweight='bold')
plt.ylabel('sin(x)', fontweight='bold')
plt.grid(True)

# plotly graph of X
fig2 = py.graph_objects.Figure()
fig2.add_trace(py.graph_objects.Scatter(x=x, y=np.sin(x), mode='lines', name='sin(x)'))
fig2.add_trace(py.graph_objects.Scatter(x=x, y=np.cos(x), mode='lines', name='cos(x)'))
fig2.update_layout(title='Plotly Graph', xaxis_title='x', yaxis_title='sin(x)')
#fig2.update_layout(legend=dict(
    #yanchor="top",
    #y=0.99,
   #xanchor="left",
    #x=0.01
#)

# ploting a graph with seaborn
# sns.set_theme(style="darkgrid")
# tips = sns.load_dataset("tips")

x1 = np.linspace(0, 20, 100)
y1 §= np.sin(x1) + np.random.randn(100) * 0.1
fig3 = sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)



# ---| ALL FUNCTIONS |---

# Header section

with st.container():
    st.title("Streamlit App")
    st.subheader("This is a Test web app for LeWagon Team Energy")
    st.write("This is a test app for LeWagon Team Energy to test Streamlit")
    st.write("[Le Wagon Home Page](https://www.lewagon.com)")

with st.container():
    st.write("---")
    left_column,center_colum, right_column = st.columns(3)
    with left_column:
        st.write('''
        This is the left column.
        it is 50% of the page but
        im sure we could make it bigger
        ''')
    # This is an Anamated Lottie file from LottieFiles.com that is beings shown of the checkbox is checked.
    with center_colum:
        if st.checkbox(label="Show Somthing Cool", value=False, key="Show_The_Lottie", help=None, on_change=None, args=None, kwargs=None):
            st_lottie(lottie_coding_Pyraminx_Shape_Lottie_Animation, height=300, key="coding", speed=0.8)
    with right_column:
        st.empty()

with st.container():
    st.write("---")
    st_lottie(lottie_coding_Data_Science_Animation, height=600)

with st.container():
    if st.button(label="Click me", key="Clicked", help=None, on_click=None, args=None, kwargs=None, disabled=False):
        st.write("You clicked the button")

with st.container():
    st.selectbox('Pick one', ['cats', 'dogs'])
    st.write("---")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write("How are you?")
        drop_Down_1 = st.selectbox('Pick one', ["","I'm good", "I'm ok", "I'm not good"])
        if drop_Down_1 == "I'm good":
            st.write("That's good to hear")
        elif drop_Down_1 == "I'm ok":
            st.write("That's ok to hear")
        elif drop_Down_1 == "I'm not good":
            st.write("That's not good to hear")
        else :
            st.write("Please select an option")
    with col2:
        st.write("Column 2")
    with col3:
        st.write("Column 3")
    with col4:
        st.write("Column 4")
    with col5:
        st.write("Column 5")

# graphst section -- Matplotlib
with st.container():
        st.write("This is a matplotlib graph")
        st.pyplot(fig)

# graphst section -- Plotly
with st.container():
    st.write("This is a plotly graph")
    st.plotly_chart(fig2)
    # print plotly graph to png file
    if st.button(label="Print Plotly Graph?", key="Print_Plotly_Graph", help=None, on_click=None, args=None, kwargs=None, disabled=False):
        fig2.write_image("plotly_graph.png")

# contact form section from form submit
# link for info here --> https://formsubmit.co/
with st.container():
    st.write("---")
    contact_form = '''
    <form action="https://formsubmit.co/jordan.lee.harris@icloud.com" method="POST">
        <input type="hidden" name="captcha" value="false" />
        <input type="text" name="name" required>
        <input type="email" name="email" required>
        <textarea name="Anything else you would like to say?" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

# Show a dataframe
#with st.container():
    # st.dataframe(my_dataframe)
    # st.table(data.iloc[0:10])
    # st.json({'foo':'bar','fu':'ba'})
    # st.metric('My metric', 42, 2)

# footer section with contrabuters and links
with st.container():
    st.write("---")
    col1, col2, col3= st.columns(3)

    with col1:
        st.write("Built badly by Jordan Harris")
        st.write("Lets hope team energy can do better")
    with col2:
        st.write("Lets hope team energy can do better")
    with col3:
        st.write("Lets hope team energy can do better")
