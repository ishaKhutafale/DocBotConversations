import streamlit as st
import sqlite3

DATABASE_NAME = 'user_database.db'

# Function to initialize database
def initialize_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

# Function to insert user into the database
def insert_user(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Function to check if username exists in the database
def check_username(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

# Initialize the database
initialize_database()

# Main app function
def app():
    st.title("User Authentication System")
    
    # Simple navbar for login and register
    nav_option = st.sidebar.radio("Navigation", ["Login", "Register"])

    if nav_option == "Register":
        st.subheader("Register New User:")
        new_username = st.text_input("Enter Username:")
        new_password = st.text_input("Enter Password:", type="password")
        if st.button("Register"):
            if not new_username or not new_password:
                st.warning("Please enter both username and password.")
            elif len(new_username) < 4 or len(new_password) < 6:
                st.warning("Username should be at least 4 characters long and password should be at least 6 characters long.")
            else:
                # Check if username already exists
                if check_username(new_username):
                    st.warning("Username already exists. Please choose a different one.")
                else:
                    insert_user(new_username, new_password)
                    st.success("Registration successful! You can now log in.")

    elif nav_option == "Login":
        st.subheader("Login:")
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        if st.button("Login"):
            if not username or not password:
                st.warning("Please enter both username and password.")
            else:
                user = check_username(username)
                if user:
                    saved_password = user[2]
                    if password == saved_password:
                        st.success(f"Welcome back, {username}! Now you can go to upload PDFs.")
                        st.session_state.user = username  # Store username in session state
                    else:
                        st.error("Incorrect password. Please try again.")
                else:
                    st.error("Username not found. Please register if you are a new user.")

if __name__ == "__main__":
    app()
