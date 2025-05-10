import streamlit as st

c0, c1 = st.columns([2, 4])

with c0:
    st.title("Name of our app")
    st.write("This is some text. To be replaced")
    st.markdown("")
    st.subheader("📌 User input")

    with st.form(key="my_form_input"):
        c2, c3 = st.columns([1, 5])
        with c2:
            # Collect models choice
            st.markdown("💾 **-- Select the model --**")
            option_fss = st.checkbox("EDITA - FSs",
                                     help="This is the model that analyzes your text in the 'Featured Snippets' context",
                                     disabled=True)
            option_serps = st.checkbox("EDITA - SERPs",
                                       help="This is the model that analyzes your text in the 'Search Engine Ranking "
                                            "Pages' context")

            models = []
            if option_fss:
                models.append("EDITA - FSs")
            if option_serps:
                models.append("EDITA - SERPs")
            # Collect buckets choice
            st.markdown("🪣 **-- Select the buckets --**")
            option_coh = st.checkbox('Coherence',
                                     help="""This section provides an information about average relevancy between 
                                     consecutive sentences in different text-meta data. """
                                     )
            option_cou = st.checkbox('Counts',
                                     help="""This section provides an information about elementary parts of speech, 
                                     like characters, words, sentences, difficult words, but also words with single and 
                                     multiple syllables. """
                                     )
            option_gra = st.checkbox('Grammar',
                                     help="""This section provides a detailed information about grammatical aspect of 
                                     your text-meta data. """
                                     )
            option_rea = st.checkbox('Readability',
                                     help="""This section provides a detailed information about readability level of your 
                                     text-meta data. It is based on tests performed in US. """
                                     )
            option_sen = st.checkbox('Sentiment',
                                     help="""This section provides an information on the polarity and objectivity of your 
                                     text-meta data. """
                                     )


with c1:
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