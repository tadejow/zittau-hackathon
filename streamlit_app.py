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
        st.title(current_task)

        st.markdown(
            """
            *You are now standing on the **Brücke über die Mandau**, looking in the direction of **Rumburk**, where our story begins...*

            Over there, the **Mandau** winds its way through **three countries**: the **Czech Republic**, **Germany**, and **Poland**.  
            A peaceful stream at first glance… but don’t be fooled.  
            This river has seen things. **Big things.**
            """
        )

        st.markdown("---")

        st.markdown(
            """
            💥 **Time Capsule: 1880**  
            The sky turned dark. The rains didn’t stop.  
            Within days, over **300 houses were destroyed**.  
            One of the worst floods in Mandau’s history.  

            *Did the citizens see it coming?*  
            Exactly. They didn’t.
            """
        )

        st.markdown("---")

        st.markdown(
            """
            After 150 years, we've learned our lesson.  
            We've built **automated alarms**, installed **emergency sirens**, and created **mobile apps** to warn us when nature gets angry.
            """
        )

        st.markdown(
            """
            🧠 **But let's try to guess** — how much time do we actually have to prepare for a flood?
            """
        )

        st.markdown(
            """
            🌧️ *Imagine this:*  
            Heavy rain just started falling… **20 km upstream** from where you stand.  
            The water’s rising.  
            The clock is ticking.  
            """
        )

        st.image('burgers_simulation_with_source.gif')

        st.markdown(
            """
            You've just witnessed how quickly disaster can strike.  

            In the **19th century**, people had no warning.  
            **Today, _you_ are the warning.**  
            The tools are in your hands — the **data**, the **alerts**, the **instincts**.

            💡 *But will you use them in time?*
            """
        )

        st.markdown(
            """
            This was just the beginning.  
            The **rain has started**.  
            The **river remembers**.  
            """
        )

        st.markdown("**Are you ready for what comes next?**")
        st.markdown("👉 **Turn around. And go with the flow.**")