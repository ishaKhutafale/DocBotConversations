import streamlit as st
import os
from tempfile import NamedTemporaryFile
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, set_global_service_context
from llama_index.embeddings.gradient import GradientEmbedding
from llama_index.llms.gradient import GradientBaseModelLLM
import sqlite3

DATABASE_NAME = 'user_database.db'

# Function to initialize chat history database for a user
def initialize_chat_history_database(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS {username}_chat_history 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT)''')
    conn.commit()
    conn.close()

# Function to insert chat message into the database
def insert_chat_message(username, question, answer):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(f"INSERT INTO {username}_chat_history (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()


# Main app function
def app():
    st.title("Doc Bot Conversations")

    # Check if user is logged in
    if 'user' not in st.session_state:
        st.warning("Login to upload PDF:)")
        st.stop()
    

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "activate_chat" not in st.session_state:
        st.session_state.activate_chat = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Initialize chat history database for the logged-in user
    initialize_chat_history_database(st.session_state.user)

   # Display chat history in sidebar for the logged-in user
    st.sidebar.subheader("Chat History")
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {st.session_state.user}_chat_history")
    chat_history = c.fetchall()
    for msg in chat_history:
        st.sidebar.text(f"Q: {msg[1]}\nA: {msg[2]}")
    conn.close()

    os.environ['GRADIENT_ACCESS_TOKEN'] = "cDo0KlCwJywJo4kQmGDaq9pgFHbrz9om"
    os.environ['GRADIENT_WORKSPACE_ID'] = "61635c4f-f42e-4ba9-8483-63fa3973fde4_workspace"

    llm = GradientBaseModelLLM(base_model_slug="llama2-7b-chat", max_tokens=400)

    embed_model = GradientEmbedding(
        gradient_access_token=os.environ["GRADIENT_ACCESS_TOKEN"],
        gradient_workspace_id=os.environ["GRADIENT_WORKSPACE_ID"],
        gradient_model_slug="bge-large")

    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
        chunk_size=256)

    set_global_service_context(service_context)
    # Upload PDF in the middle of the page
    st.subheader('Upload Your PDF File')
    docs = st.file_uploader('⬆️ Upload your PDF & Click to process',
                            accept_multiple_files=False,
                            type=['pdf'])

    # Process button below the Upload PDF section
    if st.button('Process'):
        with NamedTemporaryFile(dir='.', suffix='.pdf') as f:
            f.write(docs.read())
            with st.spinner('Processing'):
                documents = SimpleDirectoryReader(os.path.dirname(f.name)).load_data()
                index = VectorStoreIndex.from_documents(documents,
                                                        service_context=service_context)
                query_engine = index.as_query_engine()
                if "query_engine" not in st.session_state:
                    st.session_state.query_engine = query_engine
                st.session_state.activate_chat = True

    if st.session_state.activate_chat:
        if prompt := st.chat_input("Ask your question from the PDF?"):
            with st.chat_message("user", avatar='👨🏻'):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user",
                                              "avatar": '👨🏻',
                                              "content": prompt})

            query_index_placeholder = st.session_state.query_engine
            pdf_response = query_index_placeholder.query(prompt)
            if not pdf_response.response:  # If response is empty
                cleaned_response = "Sorry, this is not mentioned in the uploaded PDF."
            else:
                cleaned_response = pdf_response.response
            with st.chat_message("assistant", avatar='🤖'):
                st.markdown(cleaned_response)
            st.session_state.messages.append({"role": "assistant",
                                              "avatar": '🤖',
                                              "content": cleaned_response})

            insert_chat_message(st.session_state.user,prompt, cleaned_response)


if __name__ == "__main__":
    app()
