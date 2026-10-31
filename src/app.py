import streamlit as st
import pandas as pd
from attendance_tracker import AttendanceTracker
from engagement_analyzer import EngagementAnalyzer
from suggestion_agent import TeachingAssistantAgent

st.set_page_config(page_title="Multimodal Attendance & Engagement Agent", layout="wide")
st.title("Multimodal Classroom Intelligence Agent")

tab1, tab2, tab3 = st.tabs(["Attendance Logs", "Engagement Dynamics", "AI Teaching Suggestions"])

with tab1:
    st.subheader("Automated Sustained Presence Tracking")
    sample_data = {
        "Student ID": ["S101", "S102", "S103"],
        "Name": ["Aman Sharma", "Rhea Patel", "Karan Verma"],
        "Sustained Duration": ["35s", "42s", "31s"],
        "Status": ["Present", "Present", "Present"]
    }
    st.table(pd.DataFrame(sample_data))

with tab2:
    st.subheader("Real-Time Behavioral Analytics")
    st.metric(label="Overall Classroom Engagement Score", value="78.4%", delta="+3.2%")
    st.line_chart([65, 70, 72, 85, 80, 78, 82, 78])

with tab3:
    st.subheader("AI Decision-Support System")
    suggestions = TeachingAssistantAgent.generate_suggestions(78.4, 12.0)
    for s in suggestions:
        st.info(f"💡 {s}")
