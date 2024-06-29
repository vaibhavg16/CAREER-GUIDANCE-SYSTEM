import streamlit as st
import sqlite3
from sqlite3 import Error
import subprocess
import bcrypt

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# Function to validate user credentials
def validate_credentials(conn, email, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    if user:
        hashed_password = user[3]  # Assuming hashed password is stored in the fourth column
        # Check if the provided password matches the hashed password from the database
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("User:", user)  # Debugging statement
            return user
    return None

# Main function
def main():
    st.title("User Login")

    # Create or connect to the database
    database = "registration.db"
    conn = create_connection(database)

    if conn is None:
        st.error("Error! cannot create the database connection.")
        return

    # User login form
    with st.form(key='login_form'):
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            if email and password:
                user = validate_credentials(conn, email, password)
                if user:
                    st.success(f"Welcome, {user[1]}!")
                    # Set session state variable to indicate successful login
                    st.session_state.logged_in = True
                    # Run NextStepBot.py
                    subprocess.Popen(["streamlit", "run", "NextStepBot.py"])
                else:
                    st.error("Invalid email or password!")
            else:
                st.warning("Please fill out all fields.")

    # Register button
    if st.button("Register"):
        subprocess.Popen(["streamlit", "run", "registration.py"])

if __name__ == "__main__":
    main()
