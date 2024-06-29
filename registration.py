import streamlit as st
import sqlite3
import bcrypt
import subprocess

def create_user_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, password TEXT)''')
    conn.commit()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def add_user(conn, name, email, password):
    c = conn.cursor()
    hashed_password = hash_password(password)
    print("Adding user:", name, email)  # Print for debugging
    c.execute('''INSERT INTO users (name, email, password) VALUES (?, ?, ?)''', (name, email, hashed_password))
    conn.commit()
    print("User added successfully:", name, email)  # Print for debugging

def is_user_exists(conn, email):
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE email = ?''', (email,))
    return c.fetchone() is not None

def main():
    st.title("User Registration")

    # Create a connection to SQLite database
    conn = sqlite3.connect('registration.db')

    # Create necessary tables
    create_user_table(conn)

    # Registration form
    with st.form("registration_form"):
        st.write("Fill out the form to register:")
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.form_submit_button("Register"):
            if password == confirm_password:
                if not is_user_exists(conn, email):
                    add_user(conn, name, email, password)
                    st.success("Registration successful!")
                else:
                    st.error("User already exists with this email!")
            else:
                st.error("Passwords do not match!")
                
    

if __name__ == "__main__":
    main()
