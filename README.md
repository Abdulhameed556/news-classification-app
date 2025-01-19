# news-classification-app

Overview
=

This project is a News Classification App that uses machine learning to classify news articles as either "True" or "Fake." The model is based on a Naive Bayes Classifier trained on preprocessed text data. The application is built using Streamlit and is designed to allow users to input a news title and content, and receive a prediction about its authenticity.

Features
=

1. Text Preprocessing: The app cleans and preprocesses input text to remove noise (e.g., special characters, numbers, and stopwords).

2. Machine Learning Model: A Naive Bayes model trained on a labeled dataset of true and fake news.

3. User-Friendly Interface: Built with Streamlit to provide an interactive web application.

4. Fast Predictions: Leverages CountVectorizer for text vectorization and efficient classification.

Installation
=

- **Prerequisites**
Ensure you have the following installed:
1. Python 3.8+
2. Git
3. Pip (Python package manager)

**Steps**

- Clone the repository: git clone https://github.com/Abdulhameed556/news-classification-app.git
cd news-classification-app

- Create a virtual environment (optional but recommended): python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

**Install the required dependencies**: pip install -r requirements.txt

Usage
=

- Run the Streamlit app: streamlit run app.py

- Open the application in your web browser at http://localhost:8501.

- Input the title and content of a news article in the respective fields.

- Click the "Predict" button to see whether the news is classified as "True" or "Fake."

Dataset
=

The model was trained on a labeled dataset of true and fake news articles. The dataset contains two main features:
1. Title: The headline of the news article.
2.  Content: The body text of the news article.

- The target variable is:

**Label:** A binary classification of 1 for "True" news and 0 for "Fake" news.

Model
=

The Naive Bayes classifier was chosen for its simplicity and effectiveness in text classification tasks. Key steps include:

Text Vectorization: The CountVectorizer transforms text data into a numerical representation (bag-of-words model).

Training: The model learns probabilities of word occurrences for each class (True/Fake).

Prediction: Given new input, the model calculates the likelihood of each class and predicts the most probable one.

File Structure
=

- **app.py:** The Streamlit app script.

- **model.pkl:** The saved Naive Bayes model.

- **vectorizer.pkl:** The saved CountVectorizer.

- **requirements.txt:** List of Python dependencies.

- **README.md:** Project documentation.

Deployment
=

The app is ready for deployment using platforms like:

- Streamlit Cloud: For deploying Streamlit apps.

- Hugging Face Spaces: For hosting the app with free GPU/CPU resources.

To deploy, follow these steps:

1. Push your project to GitHub:
git add .
git commit -m "Initial commit"
git push origin main

2. Deploy on your desired platform using their guidelines.

# Future Improvements

1. Enhance the preprocessing pipeline by adding lemmatization or stemming.

2. Experiment with advanced classification models (e.g., Logistic Regression, SVM, or Transformer-based models).

3. Add more interactive features like file upload for batch predictions.

# Acknowledgments

Dataset sourced from Fake News Detection Kaggle Dataset.

Machine learning resources provided by online tutorials and documentation.

# License

This project is open-source and available under the MIT License.

