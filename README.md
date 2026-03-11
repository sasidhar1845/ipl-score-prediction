# IPL Score Prediction

This project predicts the final score of an IPL cricket match using machine learning techniques based on historical match data. The model analyzes match conditions such as batting team, bowling team, overs completed, runs scored, and wickets fallen to estimate the expected final score.

---

## Objective

The main objective of this project is to build a machine learning model that can accurately predict the final score of an IPL match using past match statistics and match conditions. This demonstrates how data science and predictive analytics can be applied in sports analytics.

---

## Dataset

The dataset used in this project contains historical IPL match data with features such as:

* Batting Team
* Bowling Team
* Current Runs
* Wickets Fallen
* Overs Completed
* Runs in Last 5 Overs
* Wickets in Last 5 Overs

Dataset file used in this project:

```
IPL_FINAL.csv
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Django (for web deployment)

---

## Machine Learning Model

The following machine learning model was used:

* Random Forest Regressor

The model was trained on historical IPL match data to predict the final score of the match based on current match conditions.

---

## Model Performance

The Random Forest Regressor model was trained using historical IPL match data and evaluated on a test dataset.

**Model Accuracy: 71%**

The model predicts the expected final score based on match parameters such as:

* Runs scored
* Overs completed
* Wickets fallen
* Batting team
* Bowling team
* Recent match performance

---

## Features

* Predict IPL match final score using machine learning
* Uses historical IPL match dataset
* Random Forest Regressor model for prediction
* Web interface built using Django
* User can input match conditions to estimate final score

---

## Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training using Random Forest Regressor
6. Model Evaluation
7. Deployment using Django Web Framework

---

## Project Structure

```
ipl-score-prediction
│
├── css
├── fonts
├── js
├── templates
│
├── IPL_FINAL.csv        # Dataset
├── IPL2.pkl             # Trained Machine Learning Model
├── M3-RFR.ipynb         # Jupyter Notebook for Model Training
│
├── views.py
├── models.py
├── forms.py
├── urls.py
├── settings.py
├── manage.py
│
└── README.md
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone [https://github.com/yourusername/ipl-score-prediction.git](https://github.com/sasidhar1845/ipl-score-prediction)
```

### 2. Navigate to the project directory

```
cd ipl-score-prediction
```

### 3. Install required libraries

```
pip install -r requirements.txt
```

### 4. Run the Django server

```
python manage.py runserver
```

### 5. Open the browser

```
http://127.0.0.1:8000/
```

---

## Results

The trained Random Forest Regressor model predicts the expected final score of the IPL match based on real-time match parameters. This demonstrates how machine learning can be applied in sports analytics to generate predictive insights.

---

## Future Improvements

* Improve prediction accuracy using advanced models
* Deploy the application using cloud platforms
* Add live match data integration
* Improve UI for better user interaction

---

## Author

**Sasidhar M**
MSc Data Science Student
Interested in Data Science, Machine Learning, and Sports Analytics
