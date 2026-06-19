# ✨ Easy Notes: AI-Powered Document Summarizer

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=flat-square&logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3">
</p>

Easy Notes is a web-based document summarization platform designed to help users quickly understand the contents of lengthy documents, PDFs, and images using Google's advanced Gemini AI.

The platform allows users to upload various file formats and instantly receive an elaborated, easy-to-understand summary covering every major topic and point. 

By combining modern web technologies with the Gemini API, Easy Notes transforms complex and long documents into simple, actionable, and beautifully formatted notes.

---

# 🎯 Problem Statement

In today's fast-paced world, individuals and professionals often struggle to find the time to read through lengthy documents, reports, and dense text files.

Easy Notes addresses this challenge by providing an intuitive platform where users can upload documents and instantly receive a comprehensive, AI-generated summary, saving time and improving information retention.

---

# 🌟 Key Features

## 📂 Multi-Format File Uploads

* Supports text documents (.txt)
* Supports Microsoft Word documents (.docx)
* Supports PDF files (.pdf)
* Supports Images (.png, .jpg, .jpeg)
* Secure file handling and strict extension validation

## 🤖 AI-Powered Summarization

* Powered by Google's Gemini 3.5 Flash
* Extracts major topics and key points
* Explains content in simple, easy-to-understand language
* Processes both text and image formats seamlessly

## ✨ Attractive User Interface

* Modern, minimal flat design
* Dotted-grid aesthetics with soft drop-shadows
* Built-in markdown-to-HTML rendering
* Dedicated, distraction-free result page

---

# 🏗️ Technical Architecture

## 1. File Processing Engine

The backend handles secure file uploads using Flask-WTF and Werkzeug.

It processes user inputs and securely saves files to a temporary local `uploads/` directory, actively validating file extensions before proceeding to the AI layer.

---

## 2. Artificial Intelligence Layer

The core summarization engine is powered by the Google GenAI SDK. 

Files are securely uploaded to the Gemini API, where the `gemini-3.5-flash` model analyzes the document structure and content to generate a comprehensive summary. Temporary files are immediately cleaned from the local server post-processing to conserve space.

---

## 3. UI & Markdown Presentation Layer

The presentation layer transforms Gemini's raw markdown response into a beautifully styled HTML interface. 

Using the Python `markdown` library and Jinja templating, the app parses bold text, headers, and lists dynamically within a modern CSS layout so the user receives a highly readable document.

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* Vanilla CSS
* Jinja2 Templating
* Google Fonts (Inter)

## Backend

* Python 3
* Flask
* Flask-WTF (Form Validation)
* Werkzeug (Secure File Handling)
* Markdown (Text Parsing)

## Artificial Intelligence

* Google Gemini API
* Google GenAI SDK (google-genai)

---

# 📂 Project Structure

```text
geminiapi/
│
├── app.py                # Main Flask server and API logic
├── .env                  # Environment variables (API Keys)
├── requirements.txt      # Project dependencies (Optional)
├── uploads/              # Temporary file storage directory
│
├── templates/            # HTML Templates
│   ├── index.html        # Upload interface
│   └── result.html       # Summary display page
│
└── README.md
```

---

# 🚀 Getting Started

## 1. Prerequisites

Ensure you have the following installed:

* Python 3.10+
* Git
* A Google Gemini API Key

---

## 2. Clone Repository

```bash
git clone https://github.com/kunnalsinngh14/Easy-Notes.git

cd Easy-Notes
```

---

## 3. Setup Virtual Environment & Install Dependencies

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install Flask Flask-WTF python-dotenv google-genai markdown werkzeug
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_flask_secret_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 5. Setup Uploads Folder

Ensure you create an empty `uploads` directory to handle temporary files. The app will crash if this folder is missing:

```bash
mkdir uploads
```

---

## 6. Run the Application

```bash
python app.py
```

The application will start running on your local server. Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository, open issues, and submit pull requests to improve Easy Notes.

---

© 2026 Kunal Singh
