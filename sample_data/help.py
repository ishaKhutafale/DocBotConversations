import streamlit as st

def app():
    st.title("Help - PDF Chatbot")

    # Box 1: Introduction
    st.subheader("Introduction")
    intro_content = """
    Welcome to the help page for our PDF Chatbot project! Here you will find information on how to use the chatbot effectively.
    """
    st.info(intro_content)

    # Box 2: How to Use
    st.subheader("How to Use")
    how_to_use_content = """
    1. **Upload PDF:** Start by uploading a PDF document using the file uploader widget on the sidebar.
    2. **Chat with the Bot:** Once the PDF is uploaded, you can start interacting with the chatbot by typing your questions in the input box provided.
    3. **Ask Questions:** Ask questions related to the content of the PDF document. The chatbot will try to provide relevant answers based on the document's content.
    4. **Receive Answers:** The chatbot will respond to your questions with relevant information extracted from the uploaded PDF.
    """
    st.success(how_to_use_content)

    # Box 3: Tips for Interaction
    st.subheader("Tips for Interaction")
    interaction_tips_content = """
    - **Be Specific:** Ask questions that are specific and relevant to the content of the PDF document.
    - **Ask Clearly:** Phrase your questions clearly to help the chatbot understand and provide accurate answers.
    - **Try Different Queries:** If the chatbot doesn't understand your question or provides an incorrect answer, try rephrasing the question or asking it in a different way.
    - **Review Answers:** Verify the information provided by the chatbot to ensure accuracy.
    """
    st.warning(interaction_tips_content)

    # Box 4: Example Questions and Note
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Example Questions")
        example_questions_content = """
        - What is the introduction about?
        - Can you summarize the key points of Chapter 3?
        - Who is the author of this document?
        - When was this document published?
        - What are the main topics covered in Section 2?
        """
        st.info(example_questions_content)

    with col2:
        st.subheader("Note")
        note_content = """
        This chatbot relies on text extraction techniques from PDF documents. Accuracy may vary based on the quality and content of the uploaded PDF.
        """
        st.error(note_content)

if __name__ == "__main__":
    app()
