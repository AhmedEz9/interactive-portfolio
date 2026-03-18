import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# --- HELPER FUNCTION FOR LOTTIE ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a cool coding animation from LottieFiles
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# 1. PAGE SETUP
st.set_page_config(page_title="Ahmed Ezzaroui - Portfolio", page_icon="💻", layout="wide")

# FIX: Force page to load at the top instead of scrolling to the chat box
st.components.v1.html(
    """
    <script>
        window.parent.document.querySelector('.main').scrollTop = 0;
    </script>
    """,
    height=0
)

# --- VISUAL UPGRADE: PREMIUM MODERN UI & GLASSMORPHISM ---
st.markdown("""
<style>
    /* Sleek Frosted Glass Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.4) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    /* Modern Project Expanders */
    .streamlit-expanderHeader {
        background-color: rgba(30, 41, 59, 0.5) !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        transition: 0.3s ease;
    }
    .streamlit-expanderHeader:hover {
        border-color: #38BDF8 !important;
        background-color: rgba(30, 41, 59, 0.8) !important;
    }
    /* Clean, Professional Buttons */
    [data-testid="stFormSubmitButton"] button, [data-testid="stDownloadButton"] button {
        background-color: #38BDF8;
        color: #0F172A;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    [data-testid="stFormSubmitButton"] button:hover, [data-testid="stDownloadButton"] button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(56, 189, 248, 0.4);
        color: #0F172A;
    }
</style>
""", unsafe_allow_html=True)
# ----------------------------------------

# --- WELCOME NOTIFICATION (Only shows once per visit) ---
if "welcomed" not in st.session_state:
    st.toast("Welcome to Ahmed's Digital Portfolio! 🚀", icon="👋")
    st.session_state.welcomed = True

# 2. SIDEBAR
st.sidebar.title("Contact Information")
st.sidebar.write("📧 ahmed.ezzaroui@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/ahmed-ezzaroui/)")
st.sidebar.write("💻 [GitHub](https://github.com/AhmedEz9)")

# Live GitHub Stats API Fetch
st.sidebar.divider()
st.sidebar.header("Live GitHub Stats 📊")
try:
    github_response = requests.get("https://api.github.com/users/AhmedEz9")
    if github_response.status_code == 200:
        github_data = github_response.json()
        st.sidebar.write(f"📦 **Public Repos:** {github_data.get('public_repos', 0)}")
        st.sidebar.write(f"👥 **Followers:** {github_data.get('followers', 0)}")
    else:
        st.sidebar.write("Stats temporarily unavailable.")
except Exception:
    st.sidebar.write("Could not connect to GitHub.")

st.sidebar.divider()
st.sidebar.header("Languages")
st.sidebar.write("🗣️ English, Finnish, French")

st.sidebar.divider()
# Download button for CV
try:
    with open("cv.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download CV (PDF)",
            data=file,
            file_name="Ahmed_Ezzaroui_CV.pdf",
        )
except FileNotFoundError:
    st.sidebar.warning("Note: cv.pdf not found in the application folder.")

# 3. MAIN SECTION - INTRO 
left_col, right_col = st.columns(2)

with left_col:
    st.title("Ahmed Ezzaroui 👋")
    st.subheader("ICT Engineering Student at Metropolia UAS | Helsinki, Finland")
    st.write("**Full Stack Developer specializing in React, Node.js & AWS.**")
    st.write("*Passionate about AI Integrations and Cloud Architecture.*")
    
    # --- VISUAL UPGRADE: IMPACT METRICS (Replaced the text quote) ---
    st.write("") # Add a little spacing
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Featured Projects", value="4")
    m2.metric(label="Certifications", value="5")
    m3.metric(label="Tech Stack", value="10+ Tools")
    st.write("") # Add a little spacing
    # ----------------------------------------------------------------

    st.write("""
    *Note: This portfolio is my project for the "New Technologies" course. I built this application 
    entirely using Python and the Streamlit library to explore rapid Low-Code development.*
    """)

with right_col:
    # Display the animation
    if lottie_coding:
        st_lottie(lottie_coding, height=300, key="coding")

st.divider()

# 4. SKILLS & CERTIFICATES SECTION
st.header("Technical Skills & Certificates 🛠️")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Skill Level")
    skills_data = pd.DataFrame({
        "Skill": ["React/Next.js", "Node.js", "AWS/Azure", "Python/Streamlit", "Docker"],
        "Proficiency (%)": [85, 80, 80, 75, 70]
    })
    skills_data.set_index("Skill", inplace=True)
    st.bar_chart(skills_data)

with col2:
    st.subheader("Certificates 📜")
    st.write("✔️ **AWS Academy Graduate** - Introduction to Cloud")
    st.write("✔️ **AWS** - Building Serverless Applications")
    st.write("✔️ **Cisco** - Networking Essentials")
    st.write("✔️ **Cisco** - Certified Network Associate Routing and Switching (CCNA)")
    st.write("✔️ **Microsoft** - Certified Professional (MCP)")

st.divider()

# 5. PROJECTS SECTION
st.header("Featured Projects 🚀")

category = st.radio(
    "Filter projects by category:",
    ["All", "Full Stack & Web", "AI & Innovation", "Python & Low-Code"],
    horizontal=True
)

st.write("---")

if category in ["All", "Full Stack & Web"]:
    with st.expander("🏥 HyMy-kylä Feedback System"):
        st.write("**Client:** Metropolia UAS")
        st.write("**Stack:** React, Vite, Tailwind CSS, Node.js, MongoDB")
        st.write("A full-stack digitalization project to streamline the feedback process for Metropolia’s wellbeing services.")
        st.write("- **Frontend:** Responsive & accessible UI built with React + Vite.")
        st.write("- **Backend:** Robust RESTful API handling data submission and administration.")

    with st.expander("💬 Chatly - Real-Time Chat App"):
        st.write("**Stack:** Node.js, Socket.IO, Azure")
        st.write("A real-time messaging application supporting custom rooms and nicknames.")

    with st.expander("📈 ProgressMate"):
        st.write("**Stack:** React / Web App")
        st.write("A recent project developed to help track progress and manage workflows effectively.")

if category in ["All", "AI & Innovation"]:
    with st.expander("🤖 Nokia Feedback Swiper"):
        st.write("**Client:** Nokia Oyj (Innovation Project)")
        st.write("**Stack:** Next.js, OpenAI API, Docker")
        st.write("An AI-powered feedback tool developed for the Nokia Garage event.")
        st.write("- **Features:** Tinder-style swipe interface for quick user engagement.")
        st.write("- **AI Integration:** Uses OpenAI API to analyze sentiment from user feedback.")

if category in ["All", "Python & Low-Code"]:
    with st.expander("🌐 Interactive Portfolio (This site)"):
        st.write("**Technologies:** Python, Streamlit, Pandas, REST APIs")
        st.write("A modern web application built as a 'Business Card' project to demonstrate my ability to quickly learn and deploy new technologies.")

st.divider()

# 6. AI ASSISTANT SECTION 
st.header("Ask My AI Assistant 🤖")
st.write("Want to know more? Ask my virtual assistant about my background!")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm Ahmed's AI assistant. Ask me about his skills, projects, or background!"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("I am AI Assist. Ask me anything about Ahmed?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = "I'm just a simple demo bot, but you can reach Ahmed directly using the contact form below!"
    prompt_lower = prompt.lower()
    
    if "skill" in prompt_lower or "react" in prompt_lower or "python" in prompt_lower:
        response = "Ahmed specializes in Full Stack development with React, Node.js, and AWS. He's also currently building data-driven apps with Python and Streamlit!"
    elif "project" in prompt_lower or "hymy" in prompt_lower or "nokia" in prompt_lower:
        response = "His featured projects include the HyMy-kylä Feedback System (React/Node) and the AI-powered Nokia Feedback Swiper. Check out the Projects section above for details!"
    elif "hire" in prompt_lower or "work" in prompt_lower or "contact" in prompt_lower:
        response = "Ahmed is always open to new opportunities! You can download his CV from the sidebar or send him a message below."

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.divider()

# 7. CONTACT FORM
st.header("Contact Me 📬")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            st.success(f"Thank you for your message, {name}! (Note: This is a demo form for the course.)")
            st.balloons() 
        else:
            st.error("Please fill in all the fields before submitting.")