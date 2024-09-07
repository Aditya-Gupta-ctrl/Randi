import streamlit as st
import streamlit_antd_components as sac


# Set page config
st.set_page_config(
    page_title="lund Hub",
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
        # App title
        st.title("Python Overview")
        
        # Introduction
        st.markdown("""
        Python is a high-level, general-purpose programming language known for its simplicity, readability, and versatility. It's widely used in various fields, including web development, data science, machine learning, and automation.
        """)
        
        # Key features
        st.subheader("Key Features")
        st.write("- **Readability:** Python's syntax is clean and easy to understand.")
        st.write("- **Versatility:** It can be used for a wide range of tasks.")
        st.write("- **Large Community:** Python has a vast and active community.")
        st.write("- **Cross-Platform Compatibility:** Python code can run on different operating systems.")
        
        # Basic concepts
        st.subheader("Basic Concepts")
        st.markdown("""
        * **Variables:** Used to store data (e.g., numbers, text, lists).
        * **Data Types:** Different types of data, such as integers, floats, strings, lists, tuples, dictionaries.
        * **Operators:** Used to perform operations (e.g., arithmetic, comparison, logical).
        * **Control Flow:** Statements that determine the order in which code is executed (e.g., if-else, loops).
        * **Functions:** Reusable blocks of code that perform specific tasks.
        * **Modules:** Files containing Python code that can be imported into other programs.
        """)
        
        # Example code
        st.subheader("Example")
        code = """
        # A simple Python program to print "Hello, World!"
        print("Hello, World!")
        """
        st.code(code, language='python')
        
        # Getting started
        st.subheader("Getting Started")
        st.markdown("""
        1. **Download and Install:** Visit the official Python website (python.org) and download the appropriate version for your operating system.
        2. **Write Code:** Use a text editor or integrated development environment (IDE) to write your Python code.
        3. **Run Code:** To execute your code, save it as a .py file and run it from the command line or your IDE.
        """)

        # Popular libraries
        st.subheader("Popular Libraries")
        st.write("- **NumPy:** For numerical computations and scientific computing.")
        st.write("- **Pandas:** For data manipulation and analysis.")
        st.write("- **Matplotlib:** For creating visualizations and plots.")
        st.write("- **Scikit-learn:** For machine learning tasks.")
        st.write("- **TensorFlow and PyTorch:** For deep learning.")


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
