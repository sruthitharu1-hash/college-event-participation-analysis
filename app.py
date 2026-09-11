import streamlit as st

st.title("🎓 College Event Participation Analysis")

events = {}

st.header("Add Event")

event_name = st.text_input("Enter Event Name")
participants = st.number_input(
    "Number of Participants", min_value=0, step=1
)

if st.button("Add Event"):
    if event_name:
        events[event_name] = participants
        st.success("Event added successfully!")
    else:
        st.warning("Please enter event name.")

st.header("📊 Event Analysis")

if events:
    st.write("### Event Details")

    for event, count in events.items():
        st.write(event, ":", count)

    total = sum(events.values())
    highest = max(events, key=events.get)
    lowest = min(events, key=events.get)
    average = total / len(events)

    st.metric("Total Participants", total)
    st.write("🏆 Highest:", highest, "-", events[highest])
    st.write("📉 Lowest:", lowest, "-", events[lowest])
    st.write("📊 Average:", average)
else:
    st.info("Add an event to see the analysis.")
