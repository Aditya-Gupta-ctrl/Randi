import streamlit as st
import streamlit_antd_components as sac
import os
import openai

# Set page config
st.set_page_config(
    page_title="chik dabak dam dam",
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
    sac.TabsItem(label='Java', icon=''),
], align='wide', size='lg' , color='grape', use_container_width=True, return_index=True)



#Home Section
if selecteds == 0:
    st.header("Welcome to Chik Dabak Dam Dam")
    st.subheader("Directly go the python for learning {others things are work in progress}")
    st.write("Backchodi maat kar lawde kaam chal raha hai na")
    print(st.secrets)

#GPT Section
if selecteds == 1:






#Python Tab Section
if selecteds == 2:
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('First Program'),
                sac.MenuItem('Data Types'),           
                sac.MenuItem('Variable'),
                sac.MenuItem('Operations'),
                sac.MenuItem('Control Flow'),
                sac.MenuItem('Function'),
                sac.MenuItem('Operations'),
                sac.MenuItem('Operations'),
                sac.MenuItem('Operations'),
            ]),
            sac.MenuItem('Cheatsheet', icon='table'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('Download Python', icon='download', description='Latest Version', href='https://www.python.org/downloads/'),
                sac.MenuItem('Download VS Code', icon='terminal', href='https://code.visualstudio.com/download'),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)
    
    if selected == 0:
        st.header("Welcome to Python")
        # App title
        st.title("Python Overview")
        
        # Introduction
        st.markdown("""
        - Python was designed and implemented by Guido van Rossum. Its journey began as a hobby in the winter months of 1989.
        - Python is a high-level, general-purpose programming language known for its simplicity, readability, and versatility. It's widely used in various fields, including web development, data science, machine learning, and automation.
        - Python, known for its simplicity and versatility, is one of the most popular programming languages today. From developing dynamic web applications to driving machine learning algorithms and handling complex data analytics. Most of the tech giants like Google, Amazon, Facebook, and Instagram rely on Python to build and maintain their cutting-edge technology solutions.
        """)

        image_url = "https://d8it4huxumps7.cloudfront.net/uploads/images/65608f420c159_what_is_python_1.jpg?d=2000x2000"
        st.image(image_url)
        
        # Key features
        st.subheader("Key Features")
        st.write("- **Interpreted Language:** This implies that Python code is executed one line at a time, making it an interpreted language. Also, in comparison to other popular languages like C, C++, Java, etc., Python code does not require compilation, making it easier to debug. In fact, an immediate format called the Bytecode is created from Python's source code.")
        st.write("- **Cross-platform Language:** Python is compatible with many operating systems/ platforms, including Windows, macOS, Linux, etc. This feature allows Python code to be portable across platforms, further allowing programmers to write code once and run it indistinguishably on several platforms.")
        st.write("- **Free and Open Source:** The language is free to download and use. Users can download Python from the official website. In addition to that, the public can also see the source code since Python is open-source.")
        st.write("- **Object Oriented:** Python has object-oriented programming features, enabling the creation and use of classes, objects, and inheritance. It encourages modular and reusable code, making it easier to develop complex applications.")
        st.write("- **Broad Standard Library:** Python contains a huge standard library with a wide selection of modules and functions, so you don't need to write any of your own code. Regular expressions, unit testing, web browsers, and other tools are all part of Python's sizable library.")
        st.write("- **GUI Support:** It is possible to create/ develop graphical user interfaces in Python by using packages like PyQt5, PyQt4, wxPython, or Tk.")
        st.write("- **Easy to Use and Maintain:** Python is pretty easy to pick up compared to other languages like C, C#, Javascript, etc. Anyone can pick up the basics of the relatively easy programming language in even a few hours or days. These features have won Python the title of one of the most user-friendly programming languages out there.")
        st.write("- **Robust:** The robustness of Python is owed to its formidable error-management capabilities, which let programmers find and fix errors in their code effectively. These features include integrated exception handling and traceback information.")
        st.write("- **Dynamically Typed:** Python is a dynamically typed language, i.e., the variable type is decided at run time (for example, int, double, long, etc.). This feature eliminates the need for users to declare the type of a variable.")
        
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
        
        
        # Getting started
        st.subheader("Getting Started")
        st.markdown("""
        1. **Download and Install:** Visit the official Python website (python.org) and download the appropriate version for your operating system.
        2. **Write Code:** Use a text editor or integrated development environment (IDE) to write your Python code.
        3. **Run Code:** To execute your code, save it as a .py file and run it from the command line or your IDE.
        """)

        # Example code
        st.subheader("Example")
        code = """
        # A simple Python program to print "Hello, World!"
        print("Hello, World!")
        """
        st.code(code, language='python')

        # Popular libraries
        st.subheader("Popular Libraries")
        st.write("- **NumPy:** For numerical computations and scientific computing.")
        st.write("- **Pandas:** For data manipulation and analysis.")
        st.write("- **Matplotlib:** For creating visualizations and plots.")
        st.write("- **Scikit-learn:** For machine learning tasks.")
        st.write("- **TensorFlow and PyTorch:** For deep learning.")


    if selected == 4:
        st.header("Python Data Type")
        st.write("Python data types offers, enabling you to manipulate and manage data with precision and flexibility. Additionally, we’ll delve into the dynamic world of data conversion with casting, and then move on to explore the versatile collections Python provides, including lists, tuples, sets, dictionaries, and arrays.")













#C Tab Section
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
