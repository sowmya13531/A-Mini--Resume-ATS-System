# A-Mini--Resume-ATS-Engine-
Resume Categorisation, Resume Parsing and Job Recommendation 
📄 Job Categorization + ATS Score Predictor (Streamlit App)
A powerful web app that analyzes resumes, predicts job categories using machine learning,NLP and calculates ATS (Applicant Tracking System) keyword match scores against job descriptions.

## 🚀 Features
✅ Upload resume in PDF format
✅ Clean and process text using NLP
✅ Predict job category using a trained ML model
✅ Compute ATS keyword match score based on job description
✅ Built with Streamlit, ready for deployment

## 🧠 Technologies Used
1.Python
2.Streamlit (for frontend)
3.Scikit-learn (for ML modeling)
4.TF-IDF (for vectorizing resume text)
5.NLTK (for tokenization and cleaning)
6.PyMuPDF (fitz) (for extracting PDF text)

## 📁 Folder Structure
resume-parser-app/
│
├── app.py                  ← Main Streamlit app
├── model.pkl               ← Trained ML model
├── tfidf.pkl               ← TF-IDF vectorizer
├── label_encoder.pkl       ← Label encoder
├── requirements.txt        ← Python dependencies
└── README.md               ← Project documentation


# 🛠️ Setup Instructions
## 🔧 1. Clone the Repo
bash
```
git clone https://github.com/sowmya13531/A-Mini--Resume-ATS-System.git
cd A-Mini--Resume-ATS-System-app
```

## 📦 2. Install Requirements
bash
```
pip install -r requirements.txt
```

## ▶️ 3. Run the App
bash
```
streamlit run app.py
```

# 🌐 Deployment
You can deploy this project for free on Streamlit Cloud:
*Push your code to GitHub
*Go to streamlit.io/cloud
*Click "New App"
*Connect your repo and set app.py as the entry point
*Deploy 🚀

# Present my app is locally deployed 
http://localhost:8501

## 📎 Sample Job Description (for testing)
We are hiring a Data Scientist to build models and extract insights from large datasets.
Skills required: Python, Machine Learning, scikit-learn, TensorFlow, Data Analysis, NLP.

## 🧠 Prediction Results
Predicted Job Category: Data Science
Model Confidence: 39.00%
ATS Keyword Match Score: 29.55%

# Future Enhancements 
- Deployed Over streamlit cloud (Network)
- Add some more features like Suggest Required Youtube Videos to improve skill development,Point out which skills needed to improve,add more than one resume to screening.

## 📩 Contact
Built by Sowmya Kanithi

Feel free to submit issues or suggestions!




