import streamlit as st
import json
import re
from logic_v2_GitHub import get_gemini_model, load_problems, check_numeric_match, analyze_and_send_report
from render_v2_GitHub import render_problem_diagram

st.set_page_config(page_title="Socratic Engineering Tutor", layout="wide")

# 1. Initialize Session State
if "page" not in st.session_state: st.session_state.page = "landing"
if "chat_sessions" not in st.session_state: st.session_state.chat_sessions = {}
if "grading_data" not in st.session_state: st.session_state.grading_data = {}
if "user_name" not in st.session_state: st.session_state.user_name = None

PROBLEMS = load_problems()

# --- Page 0: Name Entry ---
if st.session_state.user_name is None:
    st.title("🛡️ Engineering Mechanics Portal")
    with st.form("name_form"):
        name_input = st.text_input("Enter your Full Name")
        if st.form_submit_button("Access Tutor"):
            if name_input.strip():
                st.session_state.user_name = name_input.strip()
                st.rerun()
            else: st.warning("Name required.")
    st.stop()

# --- Page 1: Main Menu ---
if st.session_state.page == "landing":
    st.title(f"🚀 Welcome, {st.session_state.user_name}")
    st.info("Texas A&M University - Corpus Christi | Dr. Dugan Um")
    
    categories = {}
    for p in PROBLEMS:
        cat_main = p.get('category', 'General').split(":")[0].strip()
        if cat_main not in categories: categories[cat_main] = []
        categories[cat_main].append(p)

    for cat_name, probs in categories.items():
        st.header(cat_name)
        cols = st.columns(3)
        for idx, prob in enumerate(probs):
            with cols[idx % 3]:
                sub_label = prob.get('category', '').split(":")[-1].strip()
                if st.button(f"**{sub_label}**\n\nID: {prob['id']}", key=f"btn_{prob['id']}", use_container_width=True):
                    st.session_state.current_prob = prob
                    st.session_state.page = "chat"
                    st.rerun()

# --- Page 2: Chat Interface ---
elif st.session_state.page == "chat":
    prob = st.session_state.current_prob
    p_id = prob['id']

    if p_id not in st.session_state.grading_data:
        st.session_state.grading_data[p_id] = {'solved': set()}
    solved = st.session_state.grading_data[p_id]['solved']
    
    cols = st.columns([2, 1])
    with cols[0]:
        st.subheader(f"📌 {prob['category']}")
        st.info(prob['statement'])
        # Diagram Fix: Use st.image for fixed size (350px)
        st.image(render_problem_diagram(p_id), width=350)
    
    with cols[1]:
        st.metric("Variables Found", f"{len(solved)} / {len(prob['targets'])}")
        if st.button("⬅️ Submit Session & Score"):
            history_text = ""
            for msg in st.session_state.chat_sessions[p_id].history:
                role = "Tutor" if msg.role == "model" else "Student"
                history_text += f"{role}: {msg.parts[0].text}\n"
            st.session_state.last_report = analyze_and_send_report(st.session_state.user_name, prob['category'], history_text)
            st.session_state.page = "report_view"; st.rerun()

    # AI Initialization: Cleaned up to remove JSON requirement
    if p_id not in st.session_state.chat_sessions:
        sys_prompt = (
            f"You are a Socratic Engineering Tutor. Student: {st.session_state.user_name}. "
            f"PROBLEM: {prob['statement']}. Targets: {list(prob['targets'].keys())}. "
            "INSTRUCTIONS: 1. Ask ONE guiding question at a time. 2. No final answers. "
            "3. DO NOT USE JSON. Respond in plain text only."
        )
        model = get_gemini_model(sys_prompt)
        if model:
            session = model.start_chat(history=[])
            session.send_message("Introduce the problem and ask the first conceptual step.")
            st.session_state.chat_sessions[p_id] = session

    # Display Chat
    if p_id in st.session_state.chat_sessions:
        for message in st.session_state.chat_sessions[p_id].history:
            if "Introduce the problem" in message.parts[0].text: continue
            role = "assistant" if message.role == "model" else "user"
            with st.chat_message(role):
                # Remove internal status tags if present
                clean_msg = re.sub(r'\(Internal Status:.*?\)', '', message.parts[0].text).strip()
                # Clean any lingering JSON artifacts
                clean_msg = clean_msg.replace('{"tutor_message": "', '').replace('"}', '')
                st.markdown(clean_msg)

    # Input Logic
    if user_input := st.chat_input("Response..."):
        new_match = False
        for target, val in prob['targets'].items():
            if target not in solved and check_numeric_match(user_input, val):
                st.session_state.grading_data[p_id]['solved'].add(target)
                new_match = True
        state_info = f"\n(Internal Status: Solved={list(solved)}. NewMatch={new_match})"
        st.session_state.chat_sessions[p_id].send_message(user_input + state_info)
        st.rerun()

# --- Page 3: Report View ---
elif st.session_state.page == "report_view":
    st.title("📊 Achievement & Analysis")
    st.markdown(st.session_state.get("last_report", "No report."))
    if st.button("Return to Menu"):
        st.session_state.page = "landing"; st.rerun()
