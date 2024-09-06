import streamlit as st

# Create a text input for the user to enter their code
code_input = st.text_input("Enter your code:")

# Create a code editor for the user to write their code
code_editor = st.code_editor(code_input, language="python")

# Create an output display to show the results of the code
output_display = st.write("Output:")

# Run the code and display the output
if st.button("Run Code"):
    try:
        output = eval(code_input)
        output_display.write(output)
    except Exception as e:
        output_display.write(f"Error: {e}")
