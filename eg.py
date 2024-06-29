import streamlit as st
import sqlite3
from sqlite3 import Error

# Function to create a connection to the SQLite database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Function to fetch and display data from the database
def display_data(conn):
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        
        if rows:
            st.subheader("User Data:")
            for row in rows:
                st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
        else:
            st.write("No users found in the database.")
    else:
        st.error("Database connection is not established.")

def main():
    st.title("Display Data from Database")
    
    # Connect to the database
    database = "registration.db"
    conn = create_connection(database)
    
    # Display data from the database
    display_data(conn)

if __name__ == "__main__":
    main()
