# 🛒 ShopSmart AI — Smart Product Recommender

> An AI-powered product recommendation system built using the Naive Bayes Machine Learning algorithm.

## 🎯 Problem Statement
Users often get confused while online shopping about which product suits them best. ShopSmart AI analyzes the user's profile and automatically recommends the most relevant product.

## ✨ Features
- 🧠 Gaussian Naive Bayes algorithm
- 🎯 Personalized product recommendations
- 📊 Confidence percentage display
- 💡 Why This Recommendation explanation
- 📈 Feature contribution visualization
- 💻 Professional and responsive UI

## 🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: PHP (XAMPP)
ML Model: Python, Scikit-learn
Algorithm: Gaussian Naive Bayes
Dataset: CSV file (720 rows)

## 📁 Project Structure
index.html        → Frontend UI
style.css         → Styling
index.php         → Backend
train_model.py    → Naive Bayes Model Training
predict.py        → Prediction Engine
generate_data.py  → Dataset Generator
products.csv      → Dataset
model.pkl         → Trained Model

## ⚙️ How To Run
1. Install XAMPP
2. Place files in xampp/htdocs/shopsmart-ai
3. Open CMD and run: python train_model.py
4. Start Apache in XAMPP
5. Open browser and go to: http://localhost/shopsmart-ai/index.html

## 🧠 How It Works
Step 1: User inputs Age, Budget, Gender and Interest
Step 2: Label Encoding converts text to numbers
Step 3: Gaussian Naive Bayes model processes the input
Step 4: Best product is predicted with confidence percentage
Step 5: Why This Recommendation section explains the result

## 📊 Model Details
Algorithm: Gaussian Naive Bayes
Dataset: 720 rows, 28 products
Features: Age, Budget, Gender, Interest
Accuracy: 51% (prototype — improves with larger dataset)

## 👩‍💻 Developed By
Ayesha — Naive Bayes Machine Learning Project
