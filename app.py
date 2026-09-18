import streamlit as st
import time

# 1. Page Configuration (Title, Tab Icon, Layout)
st.set_page_config(
    page_title="Quick AI Dashboard",
    page_icon="⚡",
    layout="wide"
)

# 2. Sidebar (Controls & Inputs)
with st.sidebar:
    st.header("⚙️ App Settings")
    app_mode = st.selectbox(
        "Choose Feature:",
        ["Text Summarizer & Analyzer", "System Metric Monitor"]
    )
    st.markdown("---")
    st.caption("Built with Streamlit & Python")

# 3. Feature 1: Text & Sentiment Analyzer
if app_mode == "Text Summarizer & Analyzer":
    st.title("📝 Text Intelligence Tool")
    st.write("Enter text below to analyze character count, word density, and generate key insights.")

    user_text = st.text_area("Input your text or document snippet here:", height=150)

    col1, col2, col3 = st.columns(3)

    if st.button("🚀 Analyze Text", type="primary"):
        if user_text.strip():
            with st.spinner("Processing analysis..."):
                time.sleep(1) # Simulating fast processing
                
                word_count = len(user_text.split())
                char_count = len(user_text)
                estimated_read_time = round(word_count / 200, 2)

                # Show stats in big cards
                col1.metric("Word Count", word_count)
                col2.metric("Character Count", char_count)
                col3.metric("Est. Read Time", f"{estimated_read_time} min")

                st.success("Analysis Complete!")
                st.subheader("💡 Key Summary Preview")
                st.info(f"**First Impression:** {user_text[:120]}..." if len(user_text) > 120 else user_text)
        else:
            st.warning("Please enter some text first!")

# 4. Feature 2: System Monitor / Dashboard
elif app_mode == "System Metric Monitor":
    st.title("📊 Real-Time Metric Tracker")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Simulated Latency")
        st.metric(label="Inference Speed", value="14.2 ms", delta="-1.5 ms")
    with col2:
        st.subheader("Model Accuracy")
        st.metric(label="Validation Score", value="94.8%", delta="+2.1%")

    st.subheader("Resource Target Slider")
    power = st.slider("Select Power Limit (Watts):", min_value=25, max_value=105, value=45)
    st.write(f"Active Allocation: **{power}W**")