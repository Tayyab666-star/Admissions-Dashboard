# Admissions-Dashboard
🎓 Admissions Dashboard

An interactive Streamlit-based admissions management dashboard for universities or colleges.
It allows admins to input data manually (programs, applicants, leads, inquiries) and visualize them with dynamic charts, metrics, and a calendar heatmap.

🚀 Features

📌 Sidebar Navigation with sections:

Applications Management

Merit Management

Fees & Payments

Content Management

📝 User Input Section

Enter program names & applicant counts

Enter lead sources & leads count

Enter inquiries (student name, program, status)

📊 Dashboard Visuals

Pie chart → Applicants by program

Metric + progress bar → Application completion rate

Heatmap → Deadlines across a month

Bar chart → Leads by source

Data table → Recent inquiries

🎨 Modern UI powered by Streamlit + Plotly

📂 Project Structure
admissions_dashboard/
│── app.py          # Main Streamlit dashboard code
│── README.md       # Project documentation

⚙️ Installation

Clone or download this repo.

Install dependencies:

pip install streamlit pandas numpy plotly


Run the Streamlit app:

streamlit run app.py

🖥️ Usage

Open the app in your browser (http://localhost:8501).

Use the sidebar menu for navigation.

Enter your own data in the input fields (programs, leads, inquiries).

Dashboard updates instantly with charts and tables.

📊 Example Dashboard Layout

Applicants by Program → Pie chart

Application Completion Rate → Metric + Progress bar

Deadlines Heatmap → Calendar-style heatmap

Leads by Source → Horizontal bar chart

Recent Inquiries → Table

📝 Notes

All data entered is temporary (not stored in a database).

You can extend it with CSV/Excel file upload for real admissions data.

Can be connected to a backend database for persistence.

📜 License

This project is open-source and free to use.
