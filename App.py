import streamlit as st
import pickle
import fitz  # PyMuPDF
import re
import string
from nltk.tokenize import word_tokenize

# --- 🎨 Minimal Black Theme Styling ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: white;
    }
    .stTextArea textarea, .stTextInput input {
        background-color: #1a1a1a !important;
        color: white !important;
    }
    .stButton button {
        background-color: #333333 !important;
        color: white !important;
        border: none;
    }
    .stMarkdown h1, h2, h3, h4, h5 {
        color: white;
    }
    .css-1v0mbdj {
        background-color: #1a1a1a !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 📦 Load trained models ---
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))
clf = pickle.load(open('model.pkl', 'rb'))

# --- 🧹 Function to clean resume text ---
def clean_resume(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\b(RT|cc)\b', '', text)
    text = re.sub(r'[@#]\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.encode('ascii', 'ignore').decode()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# --- 📊 ATS keyword match score ---
def compute_ats_score(resume_text, job_desc):
    resume_words = set(word_tokenize(resume_text.lower()))
    job_words = set(word_tokenize(job_desc.lower()))
    common = resume_words.intersection(job_words)
    score = len(common) / len(job_words) * 100 if job_words else 0
    return round(score, 2)

# --- 🚀 Streamlit UI ---
st.title("📄 Job Categorization + ATS Score Predictor")

# --- ✏️ Job description input ---
job_desc = st.text_area("📌 Paste Job Description Here", height=200)

# --- 📤 Resume upload ---
uploaded_file = st.file_uploader("📤 Upload Resume (PDF only)", type=["pdf"])
resume_text = ""

if uploaded_file is not None:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            resume_text += page.get_text()

# --- 🔍 Prediction and ATS Score ---
if st.button("🔍 Analyze Resume") and resume_text:
    cleaned = clean_resume(resume_text)
    vec = tfidf.transform([cleaned])
    pred = clf.predict(vec)[0]
    conf = clf.predict_proba(vec).max() * 100
    ats_score = compute_ats_score(cleaned, job_desc)

    st.subheader("🧠 Prediction Results")
    st.write(f"**Predicted Job Category:** `{le.inverse_transform([pred])[0]}`")
    st.write(f"**Model Confidence:** `{conf:.2f}%`")
    st.write(f"**ATS Keyword Match Score:** `{ats_score}%`")

elif st.button("🔍 Analyze Resume") and not resume_text:
    st.warning("⚠️ Please upload a resume first.")
