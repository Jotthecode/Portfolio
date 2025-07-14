import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page Configuration
st.set_page_config(page_title="Jot Ajmani | Portfolio", page_icon="🧠", layout="wide")

# --- Load Lottie Animation ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Lottie Animation ---
lottie_tech = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_mjlh3hcy.json")

# --- Custom Styles ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
    button {
        padding: 8px 15px;
        background-color: #00FFD1;
        color: black;
        border: none;
        border-radius: 5px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/Jotthecode/Portfolio/main/jot_picture.png
" width="180">
    <h2 style="margin-top: 20px;">Hi, I am <span style="color: #00FFD1;">Jot Ajmani</span> 👋</h2>
    <h3>A Passionate Python Developer and Data Science Enthusiast</h3>
    <p>Third-year IT student at Shri G.S. Institute of Technology and Science, Indore</p>
    <p>I love solving real-world problems using Data Science, building backends with FastAPI, and experimenting with AI/ML.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("""

<div style='text-align: center; font-size: 18px;'>
    💼 <a href='https://www.linkedin.com/in/jot-ajmani-b9154b217' target='_blank'>LinkedIn</a> &nbsp; | &nbsp;
    💻 <a href='https://leetcode.com/u/Jotajmani/' target='_blank'>LeetCode</a> &nbsp; | &nbsp;
    🧑‍💻 <a href='https://github.com/jotthecode' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)

# --- About Section ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("## 🧠 About Me")
left_column, right_column = st.columns(2)
with left_column:
    st.write("""
        - 🔍 Solve real-world problems using Data Science  
        - 💻 Build backends with FastAPI + MongoDB  
        - 🤖 Experiment with AI/ML and participate in Kaggle competitions  
        - 📱 Develop Streamlit Based Applications using Python  
        - 🌐 Open Source Contributions in SSoC, GSSoC, ACWoC, PLDG- Cohort, SheFi  
        - 📚 Currently growing in Blockchain and Web3 with SheFi Cohort 15  
    """)
with right_column:
    st_lottie(lottie_tech, height=300, key="tech")

# --- Projects Section ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("## 💻 My Projects")

project_list = [
    {
        "title": "City Pulse - Smart City Dashboard",
        "description": "Smart city dashboard with FastAPI, Streamlit & OpenAI API.",
        "tech": ["Python", "FastAPI", "Streamlit","PyTorch","Google Trends", "OpenAI API"],
        "github": "https://github.com/Jotthecode/CITY-PULSE"
    },
    {
        "title": "E-commerce Business Analysis",
        "description": "Data analysis using Pandas, Seaborn, K-Means Clustering.",
        "tech": ["Python", "Pandas", "Seaborn", "ML"],
        "github": "https://1drv.ms/p/c/675c80f4ee9bd824/EaNOmREkMeZPuncuKu5KFccB_MnxGfGPASM1FwfO7615Wg"
    },
    {
        "title": "Karuna Darpan Healthcare Platform",
        "description": "Role-based backend for a healthcare platform.",
        "tech": ["FastAPI", "MongoDB", "Postman", "Node.js"],
        "github": "https://github.com/Jotthecode/Backend--Karuna-Darpan"
    },
    {
        "title": "SGSITS EVENT HUB",
        "description": "Event management system for SGSITS using FastAPI and React.js",
        "tech": ["FastAPI", "React.js"],
        "github": "https://github.com/Jotthecode/SGSITS-COLLEGE-EVENT-PAGE"
    },
    {
        "title": "AI-Powered Chatbot",
        "description": "Chatbot built using OpenAI API & FastAPI.",
        "tech": ["Python", "FastAPI", "OpenAI API"],
        "github": "https://github.com/Jotthecode/ChatBot"
    }
]

cols = st.columns(2)
for i, project in enumerate(project_list):
    with cols[i % 2]:
        st.markdown(f"""
            <div style='padding:10px; border: 1px solid #555; border-radius: 10px; margin-bottom: 10px; background-color: rgba(255,255,255,0.05);'>
                <h4 style='color:#00FFD1'>{project['title']}</h4>
                <p>{project['description']}</p>
                <code>{', '.join(project['tech'])}</code><br>
                <a href="{project['github']}" target="_blank">🔗 GitHub Repo</a>
            </div>
        """, unsafe_allow_html=True)

# --- Experience Section ---
st.markdown("## 💼 My Experience")

# Top 3 Experiences
st.markdown("""
**Data Analyst Intern** — *Sabudh Foundation*  
📍 Mohali (Hybrid) | 📅 Jul 2025 – Present  
• Working on real-time data analytics and hybrid data collection

**Campus Ambassador** — *E-Cell, IIT Bombay*  
📅 Jul 2025 – Present  
• Promoting startup culture through campus events  

**Web3 Scholar** — *SheFi*  
📅 Jul 2025 – Present  
• Learning Web3, DeFi, and smart contract fundamentals
""")

# Expandable section for more
with st.expander("Show more experiences"):
    st.markdown("""
**PM 5.0 Cohort Trainee** — *IIT Guwahati*  
📅 Jun 2025 – Present  
• Product Management and Analytics hands-on training

**Summer Project Intern**  
📅 May 2025 – Jun 2025  
• Built a mental health app using WHO + Kaggle data  
• Used clustering + logistic regression to predict mood and trends

**Back End Developer Intern** — *Karuna Darpan*  
📅 Jun 2025 – Present  
• Node.js + MongoDB backend for a healthcare system

**BI & Analyst Intern** — *Adharth*  
📍 Pune | 📅 May 2025 – Present  
• Built lead analysis tools with scikit-learn + Selenium  
• Created buying intent reports with dashboards

**Open Source Contributor** — *Protocol Labs (PLDG 2.0)*  
📅 Jan 2025 – Apr 2025 | Remote  
• PRs to Filecoin, Libp2p, API-related packages

**Programming Intern** — *IDEA Lab, SGSITS*  
📅 Aug 2024 – Jan 2025  
• Worked on electronics + IoT: Auto streetlights, sensing car

**GSSoC Contributor** — *GirlScript Summer of Code*  
📅 Oct 2024 – Nov 2024  
• Backend contributions to open-source projects

**ML Trainee** — *FLUXUS, IIT Indore*  
📅 Dec 2023 – Mar 2024  
• ML model development using scikit-learn and pandas
""")

# --- Certifications Section ---
st.markdown("## 🏅 My Certifications")

# Top 3 (always visible)
st.markdown("""
**Skidev Case Combat Winner** — *SkiDev Inc.*  
📅 Issued Jun 2025  
• 🧠 Skill: Data Science  
            
**Postman API Fundamentals Student Expert** — *Postman*  
📅 Issued Nov 2024  
• Skills: API Development  


**PYTHON FOR DATA SCIENCE** — *NPTEL*  
📅 Issued Apr 2025  
🎓 Credential ID: NPTEL25CS60S439000695  
• Skills: Python, Data Science, Data Visualization  
""")

# Toggle for "Show more"
with st.expander("Show more certifications"):
    st.markdown("""
    **Object Oriented Programming** — *Infosys Springboard*  
    📅 Issued Nov 2024  
    • Skills: OOP (Object-Oriented Programming)  

    **Summer Project Certificate** — *E-Cell, IIT Guwahati*  
    📅 Issued Jun 2025  
    • Skills: Data Science, UI Design, UI Prototyping  

    **MySQL (Basic)** — *HackerRank*  
    📅 Issued Aug 2024  
    🎓 Credential ID: 9e1f19489172  
    • Skills: MySQL  

    **Data Analytics and Visualisation** — *Accenture*  
    📅 Issued Jul 2024  
    🎓 Credential ID: pHJJPwEe7yD4SnLbm  
    • Skills: Data Analytics, Data Visualization  
    """)

# --- Resume Download Section ---

st.download_button("📄 Download Resume", data=open("resume-jot.pdf", "rb").read(), file_name="Jot_Ajmani_Resume.pdf")
# --- GitHub Stats Section ---
st.markdown("## 📊 GitHub Stats")
st.markdown("""
<div style="text-align: center;">
    <img src="https://github-readme-stats.vercel.app/api?username=jotthecode&show_icons=true&theme=tokyonight" width="600">

</div>
""", unsafe_allow_html=True)

# --- Contact Section ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("## 📬 Let's Connect")
contact_form = """
<form action="https://formsubmit.co/el/fapufi" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

