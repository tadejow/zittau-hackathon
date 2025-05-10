import streamlit as st

c0, c1 = st.columns([2, 4])

with c0:
    st.title("Name of our app")
    st.write("This is some text. To be replaced")


with st.expander("ℹ️ - About this app", expanded=False):
    st.markdown(
        """
        ##### Welcome to a prototype of the EDITA's user interface!

        This is the ML model that leverages different NLP techniques in order to diagnose the problems and provide 
        the optimization strategies for your text in a selected SEO scenario. 

        ##### Purpose 
        One of our first goals was to classify given textual metadata of some website within the context 
        of some specific keyphrase. As a result of this demand we have created the tool able to encode and evaluate 
        quality of object associated with some textual information (e.g. webpage and it's main content, title, 
        headers, meta data, etc.). 

        ##### Future goals 
        Once we have established the model, that is able to tell the user if his/her content is well 
        written, we want to push it even further. Since optimizing content is very time and mind consuming process, 
        we want to generate already optimized pieces of content, that user can apply in his/her website, e.g. title, 
        h1s tags or even metadata!. """
    )
    st.markdown("")

with c1:
    st.write("Some example text.")