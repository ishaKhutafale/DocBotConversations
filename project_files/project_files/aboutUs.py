import streamlit as st

def app():
    st.title("About Us")
    st.markdown("<h2>Welcome to the About Us page!</h2>", unsafe_allow_html=True)

    st.markdown("<h3>Project Description:</h3>", unsafe_allow_html=True)
    st.write("Our project is a chatbot for PDF documents. Users can upload their PDF documents and interact with the chatbot by asking questions related to the content of the PDF.")

    st.markdown("<h3>Developers:</h3>", unsafe_allow_html=True)
    st.write("This project is developed by Aveena Dange and Isha Khutafale, students at COEP Technological University.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Aveena Dange")
        st.write("- GitHub: [Aveena Dange](https://github.com/aveenadange)")
    with col2:
        st.subheader("Isha Khutafale")
        st.write("- GitHub: [Isha Khutafale](https://github.com/ishakhutafale)")

    st.markdown("<h3>Technologies Used:</h3>", unsafe_allow_html=True)
    st.write("- Streamlit: Streamlit is used for building the user interface.")
    st.write("- Python: Python programming language is used for backend development.")
    st.write("- SQLite: SQLite database is used to store user logins and their chat history.")
    st.write("- LlamaIndex and Llama2: Used for document indexing and retrieval.")
    st.write("- Gradient LLM: Used for natural language processing and chatbot functionality.")
    st.write("- HTML: HTML is used for the frontend and UI designing.")

    # Adding some styles
    st.markdown(
        """
        <style>
        h2 {
            color: #0066cc;
        }
        h3 {
            color: #008000;
        }
        .stMarkdown {
            font-family: "Arial", sans-serif;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
