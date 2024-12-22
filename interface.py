import streamlit as st
from vision import ask_about_image

def main():
    # Page configuration
    st.set_page_config(page_title="AI Vision Chat", page_icon="🤖")
    
    # Title with styling
    st.markdown("# 🤖 AI Vision Chat Assistant")
    st.markdown("---")

    # Sidebar with instructions
    with st.sidebar:
        st.markdown("### 📝 How to use")
        st.markdown("""
        1. Upload an image file 📸
        2. Ask a question about it 💭
        3. Get AI-powered insights! ✨
        """)

            # Social Media Links
        st.markdown("---")
        st.markdown("### 🌐 Connect With Me")
        st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pawan941394/)
        
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pawan941394/)
        
        [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/p_awan__kumar/)
        
        [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Pawankumar-py4tk)
        
        """)
        
        st.markdown("---")
        st.markdown("### 👨‍💻 Created by Pawan Kumar")
        
    # Main content
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.markdown("### 📤 Upload Your Image")
        uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

    with col2:
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    st.markdown("### 💭 Ask Your Question")
    user_input = st.text_input("", placeholder="What would you like to know about the image?")

    # Submit button with styling
    if st.button("🚀 Get AI Response"):
        if uploaded_file is not None and user_input:
            with st.spinner("🤔 Analyzing..."):
                try:
                    file_bytes = uploaded_file.read()
                    response = ask_about_image(file_bytes, user_input)
                    
                    # Display response in a nice container
                    st.markdown("### ✨ AI Response")
                    st.success(response)
                except Exception as e:
                    st.error(f"❌ Oops! An error occurred: {str(e)}")
        else:
            st.warning("⚠️ Please upload an image and enter your question!")

if __name__ == "__main__":
    main()