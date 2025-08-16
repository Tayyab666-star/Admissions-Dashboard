import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta

st.set_page_config(page_title="Admissions Dashboard", layout="wide")

# -------------------------
# Sidebar - Main Menu
# -------------------------
with st.sidebar:
    st.title("Main Menu")
    st.markdown("### ")
    st.subheader("Applications Management")
    st.button("Applicant Pool")
    st.button("Verify Application")

    st.subheader("Merit Management")
    st.button("Set Merit Criteria")
    st.button("Generate Merit List")

    st.subheader("Fees & Payments")
    st.button("Verify Admission Fees")
    st.button("Verify Tuition Fees")

    st.subheader("Content Management")
    st.button("Manage Content")

    st.markdown("---")
    st.success("Hi Admin!")

# -------------------------
# Header
# -------------------------
st.markdown("### Dashboard")
st.info("Login Successfully")

# -------------------------
# User Input Section
# -------------------------
st.subheader("Enter Your Data")

# Programs & applicants
programs_input = st.text_area("Enter program names (comma separated)", "BS IT, BS Math, BS CS, BBA")
programs = [p.strip() for p in programs_input.split(",")]
applicants_input = st.text_area("Enter applicants count (comma separated)", "75, 50, 60, 40")
applicants = [int(x.strip()) for x in applicants_input.split(",")]

df_programs = pd.DataFrame({"Program": programs, "Applicants": applicants})

# Leads
sources_input = st.text_area("Enter lead sources (comma separated)", "Facebook, Instagram, LinkedIn, Website, Email")
sources = [s.strip() for s in sources_input.split(",")]
leads_input = st.text_area("Enter leads count (comma separated)", "40, 55, 30, 25, 20")
leads = [int(x.strip()) for x in leads_input.split(",")]

df_leads = pd.DataFrame({"Source": sources, "Leads": leads})

# Inquiries
st.write("Add inquiry records")
names = st.text_area("Enter names (comma separated)", "Inum Noor, Bareera, Aneesha, Hira").split(",")
prog_inq = st.text_area("Enter programs (comma separated)", "BS IT, BS Math, BS CS, BBA").split(",")
status_inq = st.text_area("Enter statuses (comma separated)", "New, Follow-up, New, Resolved").split(",")

inquiries = pd.DataFrame({
    "Name": [n.strip() for n in names],
    "Program": [p.strip() for p in prog_inq],
    "Status": [s.strip() for s in status_inq]
})

# Deadlines heatmap data
start = date.today().replace(day=1)
days = [start + timedelta(days=i) for i in range(30)]
deadline_counts = np.random.randint(0, 3, size=len(days))
cal_df = pd.DataFrame({"Date": days, "Deadlines": deadline_counts})
cal_df["Date"] = pd.to_datetime(cal_df["Date"])

# -------------------------
# Dashboard Layout
# -------------------------
col1, col2, col3 = st.columns([2, 1, 2], gap="large")

with col1:
    st.subheader("Applicants by Program")
    fig_pie = px.pie(df_programs, names="Program", values="Applicants", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Completion Rate")
    completion_rate = sum(applicants) / (sum(applicants) + 50)  # example calculation
    st.metric("Applications Completed", f"{int(completion_rate*100)}%")
    st.progress(completion_rate)

with col3:
    st.subheader("Deadlines Heatmap")
    cal = cal_df.copy()
    cal["Dow"] = cal["Date"].dt.dayofweek
    cal["Week"] = cal["Date"].dt.isocalendar().week.astype(int)
    base_week = cal["Week"].min()
    cal["WeekIndex"] = cal["Week"] - base_week
    heat = go.Figure(data=go.Heatmap(
        x=cal["WeekIndex"],
        y=cal["Dow"],
        z=cal["Deadlines"],
        text=cal["Date"].dt.strftime("%Y-%m-%d"),
        hovertemplate="Date: %{text}<br>Deadlines: %{z}<extra></extra>"
    ))
    heat.update_layout(
        yaxis=dict(tickmode="array", tickvals=list(range(7)),
                   ticktext=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]),
        xaxis_title="Week",
        yaxis_title="Day",
        height=300
    )
    st.plotly_chart(heat, use_container_width=True)

st.markdown("---")

col4, col5 = st.columns([2, 2], gap="large")

with col4:
    st.subheader("Leads by Source")
    fig_bar = px.bar(df_leads, x="Leads", y="Source", orientation="h")
    st.plotly_chart(fig_bar, use_container_width=True)

with col5:
    st.subheader("Recent Inquiries")
    st.dataframe(inquiries, use_container_width=True, height=300)

st.caption("© Admissions Portal • Dynamic Dashboard")
