# 🤖 AI Vision Chat Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
AI Vision Chat Assistant is an interactive web application that allows users to upload images and ask questions about them. The application uses the Ollama Vision model to analyze images and provide intelligent responses to user queries.

## ✨ Features
- 📤 Upload any image file
- 💬 Ask questions about the uploaded image
- 🤖 Get AI-powered responses
- 🎯 Real-time analysis
- 📱 Responsive user interface

## 🛠️ Tech Stack
- Python 3.9+
- Streamlit
- Ollama API
- LLaVA Vision Model

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/pawan941394/ai-vision-chat.git
cd ai-vision-chat
```
2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Host URL Setup
Before running the application, you need to configure your Ollama host URL in `vision.py`:

1. Open `vision.py`
2. Locate the Client initialization:
```python
client = Client(
    host='Add your url here',  
    headers={'x-some-header': 'some-value'}
)
```

## 🚀 Usage

1. Install dependencies
```bash
streamlit run interface.py
```
2. Open your browser and navigate to:
```bash
[streamlit run interface.py]
(http://localhost:8501)
```
3. Upload an image and start asking questions!

## 📁 Project Structure
```bash
ai-vision-chat/
├── interface.py      # Streamlit UI implementation
├── vision.py        # Vision model integration
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```

## 📝 File Descriptions
![Python](https://img.shields.io/badge/Python-3.9%2B-blue) interface.py

  1. Contains Streamlit interface code
  2. Handles file uploads and user interactions
  3. Manages the chat interface  
  4. Displays AI responses

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) vision.py
  1. Implements Ollama vision model integration
  2. Processes image analysis
  3. Manages API communication
  4. Handles response generation

## 📦 Requirements
```bash
streamlit>=1.24.0
ollama-python>=0.1.0
```

##  👤 Author : Pawan Kumar

<a href="https://www.linkedin.com/in/pawan941394/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>  <a href="https://github.com/pawan941394/"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>  <a href="https://www.instagram.com/p_awan__kumar/"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>  <a href="https://www.youtube.com/@Pawankumar-py4tk"><img alt="YouTube" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>


## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⭐️ Show your support
Give a ⭐️ if this project helped you! 
