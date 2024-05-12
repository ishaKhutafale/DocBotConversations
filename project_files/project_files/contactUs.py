import streamlit as st
import sqlite3

DATABASE_NAME = 'user_database.db'

# Function to initialize database
def initialize_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, message TEXT)''')
    conn.commit()
    conn.close()

# Function to insert message into the database
def insert_message(name, email, message):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

# Initialize the database
initialize_database()

def app():
    st.title("Contact Us")

    # Create a sidebar for contact information
    st.sidebar.title("Contact Information")
    st.sidebar.subheader("Contact Numbers:")
    st.sidebar.write("- Aveena Dange: +91 8795640032")
    st.sidebar.write("- Isha Khutafale: +91 7685940232")
        
    st.sidebar.subheader("Email:")
    st.sidebar.write("- Aveena Dange: aveenadange@gmail.com")
    st.sidebar.write("- Isha Khutafale: ishakhutafale@gmail.com")

    st.sidebar.header("GitHub Profiles:")
    st.sidebar.write("- Aveena Dange: [GitHub Profile](https://github.com/aveenadange)")
    st.sidebar.write("- Isha Khutafale: [GitHub Profile](https://github.com/ishakhutafale)")

    st.write("Feel free to reach out to us using the contact form below.")
        
    # Contact Form
    st.subheader("Contact Form:")
    st.write("You can also send us a message directly using the form below.")

    # Form inputs
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")

    # Submit button
    if st.button("Send Message"):
        if not name or not email or not message:
            st.warning("Please fill out all fields.")
        else:
            insert_message(name, email, message)
            st.success("Message sent successfully!")

if __name__ == "__main__":
    app()
