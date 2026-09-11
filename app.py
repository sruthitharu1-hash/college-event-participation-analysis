import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="College Event Participation Analysis",
    page_icon="🎓",
    layout="wide"
)

# Sample event data
data = {
    "Event": [
        "Sports Day",
        "Cultural Fest",
        "Symposium",
        "Coding Contest",
        "Quiz Competition"
    ],
    "Participants": [120, 150, 80, 60, 90]
}

df = pd.DataFrame(data)

# Title
st.title("🎓 College Event Participation Analysis")
st.write(
    "A simple dashboard to analyze student participation "
    "in different college events."
)

st.divider()

# Sidebar
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Event Data", "Analysis", "Insights", "Conclusion"]
)

# HOME
if page == "Home":

    st.header("🏠 Home")

    st.write("""
    This project analyzes student participation in various
    college events and provides useful statistics and
    visualizations.
    """)

    st.subheader("🎯 Objective")

    st.write(
        "To analyze event participation and identify events "
        "with high and low student participation."
    )

    st.subheader("📋 Features")

    st.write("✔ Event participation data")
    st.write("✔ Total participant calculation")
    st.write("✔ Highest and lowest participation")
    st.write("✔ Average participation")
    st.write("✔ Graphical analysis")
    st.write("✔ Event insights")


# EVENT DATA
elif page == "Event Data":

    st.header("📋 Event Data")

    st.dataframe(df, use_container_width=True)

    st.subheader("➕ Add New Event")

    event_name = st.text_input("Event Name")
    participants = st.number_input(
        "Number of Participants",
        min_value=0,
        step=1
    )

    if st.button("Add Event"):
        if event_name:
            new_data = pd.DataFrame({
                "Event": [event_name],
                "Participants": [participants]
            })

            df = pd.concat([df, new_data], ignore_index=True)

            st.success("Event added successfully!")
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("Please enter event name.")


# ANALYSIS
elif page == "Analysis":

    st.header("📊 Event Participation Analysis")

    total_events = len(df)
    total_participants = df["Participants"].sum()
    highest = df["Participants"].max()
    lowest = df["Participants"].min()
    average = df["Participants"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🎪 Total Events", total_events)
    col2.metric("👥 Total Participants", total_participants)
    col3.metric("🏆 Highest", highest)
    col4.metric("📊 Average", round(average, 2))

    st.divider()

    # Bar Chart
    st.subheader("📈 Event-wise Participation")

    fig = px.bar(
        df,
        x="Event",
        y="Participants",
        title="Participants by Event"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Pie Chart
    st.subheader("🥧 Participation Distribution")

    pie = px.pie(
        df,
        names="Event",
        values="Participants",
        title="Participation Distribution"
    )

    st.plotly_chart(pie, use_container_width=True)


# INSIGHTS
elif page == "Insights":

    st.header("💡 Key Insights")

    highest_event = df.loc[
        df["Participants"].idxmax(), "Event"
    ]

    lowest_event = df.loc[
        df["Participants"].idxmin(), "Event"
    ]

    highest_value = df["Participants"].max()
    lowest_value = df["Participants"].min()

    st.success(
        f"🏆 Highest participation: {highest_event} "
        f"({highest_value} participants)"
    )

    st.warning(
        f"📉 Lowest participation: {lowest_event} "
        f"({lowest_value} participants)"
    )

    st.info(
        f"📊 Average participation across events: "
        f"{df['Participants'].mean():.2f}"
    )

    st.write(
        "These results help the college understand student "
        "participation and plan future events effectively."
    )


# CONCLUSION
elif page == "Conclusion":

    st.header("📝 Conclusion")

    st.write("""
    The College Event Participation Analysis system helps
    analyze student participation in different college events.

    It provides important statistics such as total events,
    total participants, highest participation, lowest
    participation and average participation.

    Graphical visualizations make the analysis easier to
    understand and support better planning of future college
    events.
    """)

    st.success("🎓 Project Completed Successfully!")
