import streamlit as st
import pandas as pd

# Create a title for the app
st.title("Bank Management System")

# Create a sidebar for navigation st.sidebar.title("Navigation")
nav = st.sidebar.selectbox("Select an option", ["Home", "Create Account", "Deposit", "Withdraw", "Check Balance"])

# Create a home page
if nav == "Home":
    st.write("Welcome to the Bank Management System!")

# Create a page for creating an account
elif nav == "Create Account":
    st.write("Create an account")
    name = st.text_input("Enter your name")
    account_number = st.text_input("Enter your account number")
    initial_balance = st.number_input("Enter your initial balance")
    if st.button("Create Account"):
        # Add the account to a database or a CSV file
        st.write("Account created successfully!")

# Create a page for depositing money
elif nav == "Deposit":
    st.write("Deposit money")
    account_number = st.text_input("Enter your account number")
    amount = st.number_input("Enter the amount to deposit")
    if st.button("Deposit"):
        # Update the balance in the database or CSV file
        st.write("Deposit successful!")

# Create a page for withdrawing money
elif nav == "Withdraw":
    st.write("Withdraw money")
    account_number = st.text_input("Enter your account number")
    amount = st.number_input("Enter the amount to withdraw")
    if st.button("Withdraw"):
        # Update the balance in the database or CSV file
        st.write("Withdrawal successful!")

# Create a page for checking the balance
elif nav == "Check Balance":
    st.write("Check balance")
    account_number = st.text_input("Enter your account number")
    if st.button("Check Balance"):
        # Retrieve the balance from the database or CSV file
        st.write("Your balance is $1000")
