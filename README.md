# 🧠 Analyseur Sentimental — Tweet Sentiment Analyzer

A machine learning web app that analyzes the sentiment of text (tweets or any message) and classifies it as **Positive/Neutral** or **Negative**.

Built with **Python**, **Scikit-learn (SVM)**, and **Streamlit**.

---

## 🚀 Live Demo

> Deploy on [Streamlit Cloud](https://streamlit.io/cloud) for free — see deployment steps below.

---

## 📸 Features

- 🧹 Text cleaning (HTML tags, special characters, lowercasing)
- 🤖 SVM classifier trained on airline tweets
- 📊 Displays sentiment prediction with probability scores
- 🖥️ Simple and interactive Streamlit web interface

---

## 📁 Project Structure

```
sentiment-analyzer/
├── analyseursentimental.py   # Streamlit web app
├── projet.py                 # Model training script
├── model.joblib              # Pre-trained SVM model
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## ⚙️ Installation & Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-analyzer.git
cd sentiment-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run analyseursentimental.py
```

---

## 🧪 Retraining the Model (Optional)

If you want to retrain the model on your own data:

1. Place your `Tweets.csv` file in the project root
2. Run:

```bash
python projet.py
```

This will generate a new `model.joblib` file.

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"** → Connect your GitHub repo
4. Set the main file to `analyseursentimental.py`
5. Click **Deploy** 🎉

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | Support Vector Machine (SVM) |
| Kernel | Linear |
| Vectorizer | CountVectorizer (Bag of Words) |
| Training Data | Twitter US Airline Sentiment dataset |
| Classes | Negative (1) / Positive or Neutral (0) |

---

## 📦 Dependencies

See `requirements.txt`:

- `streamlit`
- `scikit-learn`
- `joblib`
- `beautifulsoup4`
- `nltk`

---

## 👤 Author

Made by **[Your Name]** — feel free to connect on [LinkedIn](https://linkedin.com) or [GitHub](https://github.com)!

---

## 📄 License

MIT License — free to use and modify.
