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
                options=("1 station / First Drop / Brücke über die Mandau",
                         "2 station /The Bleaching Fields / Mandau-Holzbrücke",
                         "Why the river is shaped as it is?",
                         "Breaking the flow of the river")
            )
            if current_task == "1 station / First Drop / Brücke über die Mandau":
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
            if current_task == "2 station /The Bleaching Fields / Mandau-Holzbrücke":
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

if current_task == "1 station / First Drop / Brücke über die Mandau":
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
        st.text("You are now standing on the Brücke über die Mandau and looking in the direction of Rumburk, where our story begins... Over there, the Mandau winds its way through three countries: the Czech Republic, Germany, and Poland. A peaceful stream at first glance… but don’t be fooled. This river has seen things. Big things.")
        st.markdown("")
        st.text("💥 Time Capsule: 1880. \n The sky turned dark. The rains didn’t stop. Within days, over 300 houses were destroyed. One of the worst floods in Mandau’s history. \n Did the citizens see it coming? \n Exactly. They didn’t.")
        st.text("")
        st.text("After 150 years we learned our lesson and found ways to warn people about natural disasters. We’ve built automated alarms, installed emergency sirens, and created mobile apps to warn us when nature gets angry.")
        st.text("🧠 But lets try to gyess, how much time do we actually have to prepare for a flood?")
        st.text("")
        st.text("🌧️ Imagine this: Heavy rain just started falling… 20 km upstream from where you stand.")
        st.text("The water’s rising.")
        st.text("The clock is ticking.")
        st.image(
            'burgers_simulation_with_source.gif'
        )
        st.text("You’ve just witnessed how quickly disaster can strike.")
        st.text("In the 19th century, people had no warning.")
        st.text("Today, you are the warning. The tools are in your hands — the data, the alerts, the instincts.")
        st.text("💡 But will you use them in time?")
        st.text("This was just the beginning.")
        st.text("The rain has started. The river remembers.")
        st.text("Are you ready for what comes next?")
        st.text("Turn around. And go with the flow.")