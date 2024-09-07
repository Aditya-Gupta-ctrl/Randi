import streamlit as st
import streamlit_antd_components as sac


# Set page config
st.set_page_config(
    page_title="VIT LearnHub",
    page_icon=":book:",
    layout="wide",
)

#Tab Menu
selecteds = sac.tabs([
    sac.TabsItem(label='Home', tag=""),
    sac.TabsItem(icon='google',tag="GPT"),
    sac.TabsItem(label='Python', icon=''),
    sac.TabsItem(label='C', icon=''),
    sac.TabsItem(label='C++', icon=''),
    sac.TabsItem(label='JAVA', icon=''),
], align='wide', size='lg' , color='grape', use_container_width=True, return_index=True)


#Menu Bar
if selecteds == 2:
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('Data Types'),           
                sac.MenuItem('Operations', icon='', description=''),
                sac.MenuItem('conditional statement', icon=''),
                sac.MenuItem('Freeze the Learning', icon=''),
            ]),
            sac.MenuItem('Cheatsheet', icon='table'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('@1', icon='', href=''),
                sac.MenuItem('@2', icon='', href=''),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)
    
    if selected == 0:
        st.header("Welcome to Python")


    if selected == 3:
        st.header("Python Data Type")
        st.write("Python data types offers, enabling you to manipulate and manage data with precision and flexibility. Additionally, we’ll delve into the dynamic world of data conversion with casting, and then move on to explore the versatile collections Python provides, including lists, tuples, sets, dictionaries, and arrays.")


#Menu Bar
if selecteds == 3:
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('Data Types'),           
                sac.MenuItem('Operations', icon='', description=''),
                sac.MenuItem('conditional statement', icon=''),
                sac.MenuItem('Freeze the Learning', icon=''),
            ]),
            sac.MenuItem('disabled', disabled=True),
            sac.MenuItem('About', icon=''),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('@1', icon='', href=''),
                sac.MenuItem('@2', icon='', href=''),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)


#Menu Bar
if selecteds == 4:
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('Data Types'),           
                sac.MenuItem('Operations', icon='', description=''),
                sac.MenuItem('conditional statement', icon=''),
                sac.MenuItem('Freeze the Learning', icon=''),
            ]),
            sac.MenuItem('disabled', disabled=True),
            sac.MenuItem('About', icon=''),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('@1', icon='', href=''),
                sac.MenuItem('@2', icon='', href=''),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)


#Menu Bar
if selecteds == 5:
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('Data Types'),           
                sac.MenuItem('Operations', icon='', description=''),
                sac.MenuItem('conditional statement', icon=''),
                sac.MenuItem('Freeze the Learning', icon=''),
            ]),
            sac.MenuItem('disabled', disabled=True),
            sac.MenuItem('About', icon=''),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('@1', icon='', href=''),
                sac.MenuItem('@2', icon='', href=''),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)
