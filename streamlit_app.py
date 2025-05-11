import streamlit as st
import pandas as pd


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

# Layout columns
c0, c1 = st.columns([2, 4])

with c0:
    st.title("🔀 FlowApp 🔀")
    st.markdown("")
    st.subheader("📌 Your Input 📌")

    with st.form(key="my_form_input"):
        # Station selector stored in session_state
        if 'current_task' not in st.session_state:
            st.session_state.current_task = "1 station / First Drop / Brücke über die Mandau"
        c2, c3 = st.columns([1.5, 0.5])
        with c2:
            # Get the current task to be displayed
            current_task = st.selectbox(
                label="💾 **-- Select the station --**",
                options=("1 station / First Drop / Brücke über die Mandau",
                         "2 station / The Bleaching Fields / Mandau-Holzbrücke",
                         "3 station / The Serpent’s Bend / German Name",
                         "4 point / The Hidden Vein / German Name",
                         "5 station / Final Checkpoint / German Name"
                         )
            )
            if current_task == "1 station / First Drop / Brücke über die Mandau":
                distance = st.slider(
                    label="How far is the source of water from the city?",
                    value=(0, 1000)
                )
                question_1 = st.selectbox(
                    label="Q1: In how many countries does the Mandau river flow?",
                    options=("One", "Two", "Three", "Four")
                )
                question_2 = st.selectbox(
                    label="Q2: What happened in 1880 along the Mandau?",
                    options=(
                        "A large drought",
                        "One of the worst floods in its history",
                        "A dam was built",
                        "The river changed course"
                    )
                )

            if current_task == "2 station / The Bleaching Fields / Mandau-Holzbrücke":
                question_1 = st.selectbox(
                    label="Q1: What was one historical use of the Mandau river?",
                    options=(
                        "Source of drinking water only",
                        "Gold mining",
                        "Textile production",
                        "Border patrol"
                    )
                )
                question_2 = st.selectbox(
                    label="Q2: What caused the decline of the bleaching fields?",
                    options=(
                        "Earthquake",
                        "Lack of workforce",
                        "Pollution from industrialization",
                        "Too much rain"
                    )
                )

            if current_task == "3 station / The Serpent’s Bend / German Name":
                obstacle = st.selectbox(
                    "Select the obstacle type",
                    options=("rectangle", "square", "triangle")
                )
                question_1 = st.selectbox(
                    label="Q1: Why did many cities form near rivers?",
                    options=(
                        "Rivers offered protection from enemies",
                        "For their beauty",
                        "For trade, farming, and fresh water",
                        "Because they were dry"
                    )
                )
                question_2 = st.selectbox(
                    label="Q2: How did humans try to control rivers?",
                    options=(
                        "By building floating bridges",
                        "By constructing weirs and straightening the path",
                        "By freezing them",
                        "By filling them with rocks"
                    )
                )

            if current_task == "4 point / The Hidden Vein / German Name":
                question_1 = st.selectbox(
                    label="Q1: What is the hidden part of the river mentioned here?",
                    options=(
                        "An underground tunnel",
                        "Groundwater",
                        "Lava",
                        "Secret canal"
                    )
                )
                question_2 = st.selectbox(
                    label="Q2: What happened in the 1970s and 1980s in the Mandau region?",
                    options=(
                        "Flooding",
                        "Chronic drought",
                        "Earthquake",
                        "Glacier melt"
                    )
                )

            if current_task == "5 station / Final Checkpoint / German Name":
                distance = st.slider(
                    label="How far is the source of water from the city?",
                    value=(0, 1000)
                )
                question_1 = st.selectbox(
                    label="Q1: What is the key lesson from the Mandau’s story?",
                    options=(
                        "Rivers are dangerous",
                        "Rivers are separate from people",
                        "Rivers are simple systems",
                        "Rivers are complex, living systems connected to many things"
                    )
                )
                question_2 = st.selectbox(
                    label="Q2: What should we do at the end of the journey?",
                    options=(
                        "Forget about the river",
                        "Stop asking questions",
                        "Go with the flow",
                        "Turn back"
                    )
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

if current_task == "2 station / The Bleaching Fields / Mandau-Holzbrücke":
    with c1:
        st.title("2️⃣ Station: The Bleaching Fields / Mandau-Holzbrücke")

        st.markdown("---")

        st.markdown(
            """
            🕰️ **Time Capsule: Threads of Industry**

            Long before **flood sirens** and **evacuation drills**,  
            the **Mandau River** was a **partner**, not a threat.
            """
        )

        st.markdown(
            """
            In the **18th and 19th centuries**, this very water **powered the local textile industry**.  
            It **shaped towns**, **fed families**, and filled the air with the scent of **steam**, **dye**, and **raw wool**.
            """
        )

        st.markdown(
            """
            🌞 **Right here**, on these fields,  
            freshly woven fabrics were spread out to **bleach under the sun** —  
            an age-old practice where **water** and **sunlight** did what **chemicals** do today.
            """
        )

        st.markdown(
            """
            💧 The river served many roles:
            - Washing **raw wool**
            - Rinsing **dyed cloth**
            - Powering **water mills**
            - Cooling **steam machines**
            - Transporting **goods downstream**
            - ...and much more
            """
        )

        st.markdown("---")

        st.markdown(
            """
            But the **city's prosperity** didn’t last long.  

            With **industrialization** came **pollution**.  
            The river ran **blue**, **red**, **yellow**...  

            The same water that once **gave life** to the industry  
            began to **poison it**.
            """
        )

        st.markdown(
            """
            🏭 **Factories closed.**  
            🌾 The **bleaching fields** were abandoned.
            """
        )

if current_task == "3 station / The Serpent’s Bend / German Name":
    with c1:
        st.title("3️⃣ Station: The Serpent’s Bend")

        st.markdown("---")

        st.markdown(
            """
            🕰️ **Time Capsule: The Flow That Changed Fates**

            You’ve probably noticed that most cities were born beside rivers.

            **Paris** rests on the *Seine*.  
            **Cairo** flourishes along the *Nile*.  
            And here, in this quiet corner of Europe, **Zittau** grew beside the *Mandau*.
            """
        )

        st.markdown(
            """
            Why?  
            Because rivers have always given us more than just water.

            They were our **lifelines** —  
            for drinking, farming, washing, and moving goods across great distances.
            """
        )

        st.markdown("---")

        st.markdown(
            """
            However, the **destiny of a city** was often shaped by the river’s path.

            Some towns **flourished** when the river flowed steadily nearby —  
            powering **grain mills**, irrigating **fields**.

            Others faced **disaster** when the water shifted course,  
            flooded farmland, or washed away bridges.
            """
        )

        st.markdown(
            """
            So humanity did what it always does best:  
            **Tried to control nature.**

            - We built **weirs** and **walls**  
            - We straightened winding curves  
            - We turned rivers into engineered lines
            """
        )

        st.markdown("---")

        st.markdown("🧠 **Now it’s your turn.**")

        st.markdown(
            """
            *(Interactive simulation here:)*  
            **How can the flow change depending on the obstacles in the river?**
            """
        )

        # Placeholder for visualization
        st.image(f"serpent_simulation_{obstacle}.gif")

        st.markdown("---")

        st.markdown(
            """
            You’ve learned a truth known for centuries:  
            **You can’t stop the river.**  
            But you can **guide** it.

            The **Mandau bends**.  
            And **history flows with it.**
            """
        )

if current_task == "4 point / The Hidden Vein / German Name":
    with c1:
        st.title("4️⃣ Point: The Hidden Vein")

        st.markdown("---")

        st.markdown(
            """
            What you see on the surface is only **half the story**.

            The **Mandau** may shimmer in the sun,  
            but beneath your feet, another river flows —  
            **invisible**, **quiet**, and just as **vital**.
            """
        )

        st.markdown(
            """
            This is the world of **groundwater**,  
            and it’s more connected to the river than you think.
            """
        )

        st.markdown("---")

        st.markdown(
            """
            When it rains too much, the Mandau **swells** and **floods**.  
            You’ve already seen how **destructive** that can be.
            """
        )

        st.markdown("🧠 **But what happens when there’s no rain at all?**")

        st.markdown(
            """
            When the **sky stays silent** and the **soil turns to dust**,  
            rivers don’t rage — they **shrink**.  
            They **vanish**.  

            And everything **below the surface** begins to suffer.
            """
        )

        st.markdown("---")

        st.markdown("🕰️ **Time Capsule: Drought in the Mandau Region**")

        st.markdown(
            """
            In the **1970s and 1980s**, on the **Czech side** of the Mandau,  
            nature flipped the script.

            Instead of **floods**, the region faced **chronic drought**.

            Meanwhile, **factories and farms** were pulling massive amounts of water  
            from underground for:
            - 🧵 textile production  
            - 🚿 washing  
            - 🌾 irrigation

            As a result:  
            - 💧 **Wells ran dry**  
            - 🌱 **Crop yields dropped**  
            - 🚛 **Water had to be imported by truck**
            """
        )

        st.markdown("---")

        st.markdown("⚡ **Imagine yourself as Zeus...**")

        st.markdown(
            """
            How might your actions change the **entire ecosystem** of the region?
            """
        )

        st.markdown(
            """
            *(Interactive simulation here:)*  
            **Set the amount of rainfall** and see the effects on  
            **water level** and **underground conditions**.
            """
        )

        # Placeholder for the visualization
        # st.image("drought_simulation_placeholder.gif")

        st.markdown("---")

        st.markdown(
            """
            You’ve seen the **Mandau in flood**.  
            Now, you’ve seen it in **drought**.

            And you’ve learned this truth:
            """
        )

        st.markdown(
            """
            💡 A **river** is not just water.  
            It’s a **network** that runs both **above** and **below** the surface.
            """
        )

if current_task == "5 station / Final Checkpoint / German Name":
    with c1:
        st.title("5️⃣ Final Checkpoint: The Journey Never Ends")

        st.markdown("---")

        st.markdown(
            """
            🏁 **Final Checkpoint: The Journey Never Ends**

            You’ve followed the **Mandau** from its first ripples to its **hidden depths**.  
            You’ve faced **floods**, **droughts**, **industry**, and **innovation**.  

            And you’ve discovered one powerful truth:
            """
        )

        st.markdown(
            """
            🌍 **The complexity of even a single river is incredible.**

            It’s a **living system** —  
            connected to **people**, **soil**, **memory**, and **future generations**.
            """
        )

        st.markdown("---")

        st.markdown(
            """
            🌊 As one river flows into another,  
            the story **never really ends**.
            """
        )

        st.markdown(
            """
            Because there’s always something more to uncover…
            - a **new hypothesis** to test  
            - a **better solution** to try  
            - a **smarter question** to ask
            """
        )

        st.markdown("---")

        st.markdown(
            """
            👉 So **go with the flow**.
            """
        )

        st.markdown(
            """
            *To be continued...*
            """
        )