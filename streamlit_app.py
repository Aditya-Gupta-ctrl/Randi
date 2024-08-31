import streamlit as st
import pandas as pd
import sqlite3
from email.message import EmailMessage
import smtplib

# Create a title for the app
st.title("Bank Management System")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
nav = st.sidebar.selectbox("Select an option", ["Home", "Create Account", "Deposit", "Withdraw", "Check Balance"])

# Create a connection to the database
conn = sqlite3.connect("bank_database.db")
cursor = conn.cursor()

# Create a table for storing account information
cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_number TEXT PRIMARY KEY,
        name TEXT,
        balance REAL
    );
""")

# Create a home page
if nav == "Home":
    st.write("Welcome to the Bank Management System!")

# Create a page for creating an account
elif nav == "Create Account":
    st.write("Create an account")
    name = st.text_input("Enter your name")
    account_number = st.text_input("Enter your account number")
    initial_balance = st.number_input("Enter your initial balance")
    email_id = st.text_input("Enter your email ID")
    if st.button("Create Account"):
        # Add the account to the database
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (account_number, name, initial_balance))
        conn.commit()
        # Send a confirmation email
        msg = EmailMessage()
        msg.set_content(f"Account created successfully! Your account number is {account_number} and your initial balance is {initial_balance}.")
        msg["Subject"] = "Account Creation Confirmation"
        msg["From"] = "your_email_id@gmail.com"
        msg["To"] = email_id
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your_email_id@gmail.com", "your_password")
            smtp.send_message(msg)
        st.write("Account created successfully!")

# Create a page for depositing money
elif nav == "Deposit":
    st.write("Deposit money")
    account_number = st.text_input("Enter your account number")
    amount = st.number_input("Enter the amount to deposit")
    if st.button("Deposit"):
        # Update the balance in the database
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = cursor.fetchone()[0]
        new_balance = balance + amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
        conn.commit()
        # Send a confirmation email
        msg = EmailMessage()
        msg.set_content(f"Deposit successful! Your new balance is {new_balance}.")
        msg["Subject"] = "Deposit Confirmation"
        msg["From"] = "your_email_id@gmail.com"
        msg["To"] = email_id
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your_email_id@gmail.com", "your_password")
            smtp.send_message(msg)
        st.write("Deposit successful!")

# Create a page for withdrawing money
elif nav == "Withdraw":
    st.write("Withdraw money")
    account_number = st.text_input("Enter your account number")
    amount = st.number_input("Enter the amount to withdraw")
    if st.button("Withdraw"):
        # Update the balance in the database
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = cursor.fetchone()[0]
        if balance >= amount:
            new_balance = balance - amount
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
            conn.commit()
            # Send a confirmation email
            msg = EmailMessage()
            msg.set_content(f"Withdrawal successful! Your new balance is {new_balance}.")
            msg["Subject"] = "Withdrawal Confirmation"
            msg["From"] = "your_email_id@gmail.com"
            msg["To"] = email_id
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login("your_email_id@gmail.com", "your_password")
                smtp.send_message(msg)
            st.write("Withdrawal successful!")
        else:
            st.write("Insufficient balance!")

# Create a page for checking the balance
elif nav == "Check Balance":
    st.write("Check balance")
    account_number = st.text_input("Enter your account number")
    email_id = st.text_input("Enter your email ID")
    if st.button("Check Balance"):
        # Retrieve the balance from the database
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = cursor.fetchone()[0]
        st.write(f"Your balance is {balance}")
        # Send a confirmation email
        msg = EmailMessage()
        msg.set_content(f"Your balance is {balance}.")
        msg["Subject"] = "Balance Inquiry"
        msg["From"] = "your_email_id@gmail.com"
        msg["To"] = email_id
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("adityagupta5436@gmail.com", "adityaloveayushi")
            smtp.send_message(msg)
        st.write("Balance sent to your email ID!")
