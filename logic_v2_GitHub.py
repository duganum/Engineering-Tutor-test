import streamlit as st
import google.generativeai as genai
import json
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_gemini_model(system_instruction):
    """Configures and returns the Gemini model using verified 2.0-flash string."""
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        return genai.GenerativeModel(
            model_name='models/gemini-2.0-flash', 
            system_instruction=system_instruction
        )
    except Exception as e:
        st.error(f"Failed to initialize Gemini: {e}")
        return None

def load_problems():
    """Loads problems from problems.json."""
    try:
        with open('problems_v2_GitHub.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading problems.json: {e}")
        return []

def check_numeric_match(user_val, correct_val, tolerance=0.05):
    """Extracts numbers and checks if answer is within 5% tolerance."""
    try:
        u_match = re.search(r"[-+]?\d*\.\d+|\d+", str(user_val))
        if not u_match:
            return False
            
        u = float(u_match.group())
        c = float(correct_val)
        
        if c == 0: 
            return abs(u) < tolerance
        return abs(u - c) <= abs(tolerance * c)
    except (ValueError, TypeError, AttributeError):
        return False

def analyze_and_send_report(user_name, problem_title, chat_history):
    """Generates AI summary with an Achievement Score and emails it to Dr. Um."""
    # Updated instruction to include scoring
    report_instruction = (
        "You are an academic evaluator. Analyze the student's Socratic tutoring session. "
        "Provide a summary of their conceptual understanding and assign an 'Achievement Score' "
        "from 0 to 10 based on their progress and accuracy."
    )
    
    model = get_gemini_model(report_instruction)
    if not model:
        return "AI Analysis Unavailable"

    prompt = (
        f"Student Name: {user_name}\n"
        f"Problem Topic: {problem_title}\n\n"
        f"Full Chat History:\n{chat_history}\n\n"
        "Please include a clear section titled 'ACHIEVEMENT SCORE: X/10' at the top of your report."
    )
    
    try:
        response = model.generate_content(prompt)
        report_text = response.text
    except:
        report_text = "Analysis generation failed, but session record exists."

    sender = st.secrets["EMAIL_SENDER"]
    password = st.secrets["EMAIL_PASSWORD"] 
    receiver = "dugan.um@gmail.com" 

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = f"Dynamics Report ({user_name}): {problem_title}"
    msg.attach(MIMEText(report_text, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        st.error(f"Email failed: {e}")
    

    return report_text

import matplotlib.pyplot as plt
import numpy as np

def render_problem_diagram(prob_id):
    """
    문제 ID를 입력받아 Matplotlib을 이용해 공학적 다이어그램을 생성합니다.
    """
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_aspect('equal')
    
    # --- 1. Statics: Free Body Diagram (S_1.1_1 ~ S_1.1_3) ---
    if prob_id == "S_1.1_1":
        # 50kg Mass suspended by two cables
        ax.plot(0, 0, 'ks', markersize=15) # Mass
        ax.annotate('', xy=(-2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='blue')) # Cable A
        ax.annotate('', xy=(1.5, 1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='green')) # Cable B
        ax.text(-1.8, 0.2, '$T_A$ (Horizontal)', color='blue')
        ax.text(0.8, 1.0, '$T_B$ ($45^\circ$)', color='green')
        ax.annotate('', xy=(0, -1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=1.5, color='red'))
        ax.text(0.1, -1.3, '$W=50kg$', color='red')

    elif prob_id == "S_1.1_2":
        # 20kg Cylinder on 30-degree incline
        theta = np.radians(30)
        # Slope
        ax.plot([-2, 2], [-2*np.tan(theta), 2*np.tan(theta)], 'k-', lw=2)
        # Cylinder
        circle = plt.Circle((0, 0.6), 0.5, color='orange', alpha=0.7)
        ax.add_patch(circle)
        # Normal Force
        ax.annotate('', xy=(0.5, 1.46), xytext=(0, 0.6), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(0.3, 1.5, '$N$', color='blue', fontsize=12)
        ax.text(-1.5, -0.5, '$30^\circ$', fontsize=10)

    # --- 2. Statics: Truss (S_1.2_1 ~ S_1.2_2) ---
    elif "S_1.2" in prob_id:
        # Simple Triangle Truss
        nodes = np.array([[0, 0], [2, 0], [1, 1.732]])
        ax.plot([0, 2, 1, 0], [0, 0, 1.732, 0], 'k-o', lw=3)
        ax.annotate('', xy=(1, 0.5), xytext=(1, 1.732), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        ax.text(1.1, 1.5, 'Load', color='red')
        ax.text(0, -0.3, 'Support A')
        ax.text(1.5, -0.3, 'Support B')

    # --- 3. Kinematics: Projectile Motion (K_2.2_1 ~ K_2.2_3) ---
    elif "K_2.2" in prob_id:
        # Projectile Trajectory
        x = np.linspace(0, 4, 100)
        y = -0.5 * (x-2)**2 + 2
        ax.plot(x, y, 'k--', alpha=0.5)
        ax.annotate('', xy=(0.5, 0.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(0.1, 0.6, '$v_0, \\theta$', color='blue')
        ax.plot(0, 0, 'ro') # Ball
        ax.set_title("Projectile Motion Path")

    # --- 4. Kinematics: Normal/Tangent & Polar (K_2.3_1, K_2.4_1) ---
    elif "K_2.3" in prob_id or "K_2.4" in prob_id:
        # Circular Path / Robotic Arm
        circle = plt.Circle((0, 0), 1.5, color='gray', fill=False, ls='--')
        ax.add_patch(circle)
        ax.plot([0, 1.06], [0, 1.06], 'k-o', lw=3) # Arm
        ax.annotate('', xy=(0.5, 1.5), xytext=(1.06, 1.06), arrowprops=dict(arrowstyle='->', color='green'))
        ax.text(0.8, 1.3, '$a_n$', color='green')
        ax.text(0.2, 0.5, '$r, \\theta$')

    # 공통 레이아웃 정리
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.axis('off')
    plt.tight_layout()
    return fig
