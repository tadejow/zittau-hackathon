import streamlit as st


def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


# User interface settings
st.set_page_config(
    page_title="FlowApp",
    page_icon="🔀",
    layout="wide"
)
_max_width_()
# Elements of the interface
c0, c1 = st.columns([2, 4])

with c0:
    st.title("🔀 FlowApp 🔀")
    st.markdown("")
    st.subheader("📌 Your Input 📌")

    with st.form(key="my_form_input"):
        c2, c3 = st.columns([1.5, 0.5])
        with c2:
            # Get the current task to be displayed
            current_task = st.selectbox(
                label="💾 **-- Select the station --**",
                options=("Flood Alert System",
                         "Drinkable water pollution",
                         "Why the river is shaped as it is?",
                         "Breaking the flow of the river")
            )
            if current_task == "Flood Alert System":
                distance = st.slider(
                    label="How far is the source of water from the city?",
                    value=(0, 1000)
                )
                question_1 = st.selectbox(
                    label="Q1: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_2 = st.selectbox(
                    label="Q2: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_3 = st.selectbox(
                    label="Q3: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_4 = st.selectbox(
                    label="Q4: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
            if current_task == "Drinkable water pollution":
                question_1 = st.selectbox(
                    label="Q1: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_2 = st.selectbox(
                    label="Q2: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_3 = st.selectbox(
                    label="Q3: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_4 = st.selectbox(
                    label="Q4: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
            if current_task == "Why the river is shaped as it is":
                question_1 = st.selectbox(
                    label="Q1: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_2 = st.selectbox(
                    label="Q2: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_3 = st.selectbox(
                    label="Q3: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_4 = st.selectbox(
                    label="Q4: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
            if current_task == "Breaking the flow of the river":
                distance = st.slider(
                    label="How far is the source of water from the city?",
                    value=(0, 1000)
                )
                question_1 = st.selectbox(
                    label="Q1: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_2 = st.selectbox(
                    label="Q2: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_3 = st.selectbox(
                    label="Q3: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
                question_4 = st.selectbox(
                    label="Q4: ",
                    options=("A1",
                             "A2",
                             "A3",
                             "A4")
                )
            submit = st.form_submit_button("✅ Submit your input")

if current_task == "Flood Alert System":
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

        st.image(
            'burgers_simulation.gif'
        )
