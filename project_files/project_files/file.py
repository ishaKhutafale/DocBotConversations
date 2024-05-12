import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import main, help, references, aboutUs, contactUs, login

class Multipage:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def home(self):
        st.title("Welcome to DocBot Conversations")

        if "messages" not in st.session_state:
            st.session_state.messages=[]
        for message in st.session_state.messages: 
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Assistant's Greeting Message
        with st.chat_message(name="assistant"):
            st.write("Hello! How can I assist you today?")

        # Lottie animation
        lottie_hello = self.load_lottieurl("lottie.json")
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center;">
                {st_lottie(lottie_hello, key="Hello", width=300, height=300)}
            </div>
            """,
            unsafe_allow_html=True
        )

    def run(self):
        st.set_page_config(page_title="DocBot Conversations", page_icon="🤖")

        # Adding logo and logo name in the navbar
        st.sidebar.title("🤖   DocBot Conversations")  

        with st.sidebar:
            app = option_menu(
                menu_title=None,
                options=["Home", "Login","Upload Pdfs", "Help", "About", "References", "Contact Us"],  # Added "Login"
                icons=["house","key","filetype-pdf", "info-circle", "file-person", "bookmark-check", "person-lines-fill"],  # Added icon for "Login"
                styles={
                    "container": {"padding": "0!important"},
                    "icon": {"color": "white", "font-size": "15px"},
                    "nav-link": {
                        "font-size": "15px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#898989",
                    },
                    "nav-link-selected": {"background-color": "#ffc00c"},
                }
            )

        if app == "Home":
            self.home()
        elif app == "Upload Pdfs":
            main.app()
        elif app == "Help":
            help.app()
        elif app == "References":
            references.app()
        elif app == 'About':
            aboutUs.app()
        elif app == 'Contact Us':
            contactUs.app()
        elif app == "Login": 
            login.app() 

    def load_lottieurl(self, filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

multipage = Multipage()

if __name__ == "__main__":
    multipage.run()
