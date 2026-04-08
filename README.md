# Spam and Ham Text Classification System

#### 1. Introduction

This project focuses on building a Natural Language Processing (NLP) system to classify SMS messages into two categories: Spam and Ham (Not Spam). The objective is to automatically detect unwanted messages using machine learning techniques and improve message filtering systems.

#### 2. Data Understanding and Cleaning
- The dataset contains 5572 SMS messages with two columns: Category and Message. There were no missing values, but 415 duplicate records were
  removed to improve data quality.
- The target variable consists of two classes: ham and spam, with a noticeable class imbalance where ham messages are more dominant.

#### 3. Exploratory Data Analysis (EDA)

During EDA, additional features such as character count, word count, and exclamation mark count were created to better understand message patterns.

##### Class Distribution of Messages
- Dataset is imbalanced with more Ham messages.
- Spam messages form a smaller portion of dataset. 
- Imbalance handled using class weights in model training.

  <img width="1286" height="582" alt="image" src="https://github.com/user-attachments/assets/ff1571dd-85df-44e4-bf89-c6ba9bd68392" />

##### Frequent Words in Spam vs Ham Messages
- Spam messages contain words like “free”, “call”, “win”, “urgent”.
- In ham messages, common daily conversation words are more frequent.
- This helps to easily understand the difference between spam and normal messages


##### Message Length Analysis 
- Spam messages are generally longer, as their median character count is higher than ham. 
- Ham messages are shorter on average but show high variability with many long outliers. 
- Spam messages are more consistent in length, indicated by a narrower box. 
- Ham contains more extreme outliers, while spam has fewer and less extreme ones. 

<img width="1280" height="573" alt="image" src="https://github.com/user-attachments/assets/c8f810e1-f6b1-4a6f-baa0-2d531827123b" />

Key insights:
- Spam messages are generally longer than ham messages.
- Spam messages contain more exclamation marks, indicating urgency or promotion.
- WordCloud visualization highlighted spam-related words like “free”, “call”, and “text”.
- Ham messages contained more conversational vocabulary.

These insights helped identify meaningful patterns for classification. Confusion matrix heatmaps were also used to evaluate model performance by analyzing true positives, true negatives, false positives, and false negatives.

#### 4. Text Preprocessing

Text preprocessing was performed to clean and standardize the messages:
- Converted text to lowercase
- Removed punctuation and stopwords
- Applied lemmatization using WordNetLemmatizer
- Retained only alphabetic tokens

The cleaned text was stored in a new column called clean_text, improving feature quality for modeling. A pipeline-based approach was used to ensure structured workflow and prevent data leakage.

#### 5. Feature Engineering (Vectorization)

The cleaned text was converted into numerical features using TF-IDF Vectorization with:
- Maximum 5000 features
- Unigrams and bigrams (1,2)

This helped capture both individual words and meaningful word combinations, improving contextual understanding while maintaining efficiency.

#### 6. Model Building

Three machine learning models were implemented using a Pipeline approach (TF-IDF + classifier combined):
- Logistic Regression (class_weight='balanced')
- Multinomial Naive Bayes
- LinearSVC (Linear Support Vector Classifier) with class balancing

Using a pipeline ensured:
- No manual feature transformation
- No data leakage
- Production-ready workflow

This approach also improved handling of class imbalance and ensured consistent preprocessing during training and prediction.

#### 7. Model Evaluation

Models were evaluated using precision, recall, F1-score, confusion matrix, and ROC-AUC score, focusing on F1-score due to class imbalance.

Best Model: LinearSVC (Linear Support Vector Classifier)

Performance:
- Precision, Recall, F1-score ≈ 0.98
- ROC-AUC Score ≈ 0.9859

This model provided the best balance between spam and ham classification.

Cross-Validation Results:

To ensure model stability, 5-fold cross-validation was performed using F1-score:
- Mean F1 Score: 0.8935
- Standard Deviation: 0.0053

This indicates consistent and reliable model performance across different data splits.

<Figure size 500x400 with 2 Axes><img width="444" height="391" alt="image" src="https://github.com/user-attachments/assets/3bbd0432-0eb2-4aeb-bd2e-d3674a12ad89" />


#### 8. Error Analysis

Misclassified messages were analyzed from the test set. Errors mainly occurred in:
- Short spam messages
- Ham messages containing spam-like words

This helped identify edge cases and limitations of the model.

#### 9. Model Saving

The final model selected was LinearSVC pipeline, saved using pickle as model.pkl.

Since TF-IDF and classifier are combined in a single pipeline, both preprocessing and prediction steps are stored together. This ensures:
- No separate vectorizer required
- Direct prediction from raw input
- Fully deployment-ready system

#### 10. Model Deployment 
The trained model was deployed using Streamlit on Hugging Face Spaces.

Steps:
- Streamlit app (app.py) created for user input
- Saved pipeline model (model.pkl) loaded in the app
- User SMS text is directly passed to the model
- Prediction displayed as Spam or Ham in real time

Since TF-IDF and classifier are integrated in a pipeline, preprocessing and prediction happen automatically during inference.

#### 10. Conclusion
- This project successfully demonstrates a complete end-to-end NLP pipeline for spam detection, including data cleaning, EDA, preprocessing, feature
  engineering, model training, evaluation, and deployment.
- The use of lemmatization, bigram TF-IDF features, and LinearSVC (Linear Support Vector Classifier) significantly improved model performance.
- The final system is deployed as a real-time web application, making it practical and ready for real-world usage.
- This solution can be applied in SMS filtering, email classification, and fraud message detection systems, improving user security and
  communication efficiency.
