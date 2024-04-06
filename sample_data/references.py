import streamlit as st

def app():
    st.title("References")
    st.write("Here are some of the resources we used in our project:")

    # Define the column layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Documentation:")
        st.write("- [Streamlit Documentation](https://docs.streamlit.io/en/stable/)")
        st.write("- [Python Documentation](https://docs.python.org/3/)")
        st.write("- [HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)")
        st.write("- [SQLite Documentation](https://sqlite.org/docs.html)")

    with col2:
        st.subheader("Tools and Libraries:")
        st.write("- [Gradient LLM](https://github.com/gradienthealth/gradient-llm)")
        st.write("- [Llama2](https://github.com/llamalab/llama2)")
        st.write("- [Llama Index](https://github.com/llamalab/llama-index)")

if __name__ == "__main__":
    app()
