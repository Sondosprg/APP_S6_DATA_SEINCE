# Semester 6 Data Analysis Dashboard

A complete interactive academic analytics dashboard built with [Streamlit], [Pandas], [Matplotlib], [Seaborn], and [Plotly Express].

This project analyzes Semester 6 modules and student grades through statistics, visualizations, and interactive tools.
The application provides automatic grade calculations, validation systems, descriptive statistics, performance analysis, and dynamic charts inside a clean Streamlit interface.

---

# live demo
https://sondosprg-app-s6-data-seince-app-do8p1t.streamlit.app/

# Preview

![Dashboard Screenshot](imgs\app.PNG)

---

# Features

## Grade Management

* Input student grades interactively
* Validation system for grades
* Automatic average calculation
* Pass / Fail detection
* Random data generator for testing

---

## Data Analysis

* cli interface with analysis in "app_S6_analysis.ipynb file"
* Interactive DataFrame display
* Subject total calculation
* Per-subject average calculation
* Descriptive statistics using Pandas `.describe()`
* TD / TP / Exam analysis
* Difficulty level statistics

---

## Technologies Used

Built using:

* Python
* jupyter
* Streamlit
* pandas
* Matplotlib
* Seaborn
* Plotly Express


---

# Project Structure

```bash
project/
│
├── data_analysis/
│   ├── data/
│   ├── __init__.py
│   ├── analysis.py
│   ├── app_S6_analysis.ipynb
│
├── .gitignore
├── app.py
├── LICENSE
├── README.md
└── requirements.txt

```

---

#  Installation

Clone the repository:

```bash
git clone https://github.com/Sondosprg/APP_S6_DATA_SEINCE.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```



#  Project Goals

This project was created to:

* Practice Data Analysis concepts
* Improve Python data manipulation skills
* Learn dashboard development with Streamlit
* Combine statistics with visualization
* Build a real-world academic analytics project


---

# Future Improvements

* add already report 
---



#  Contributing

Contributions, suggestions, and improvements are welcome.

---

# License

This project is open-source and available under the MIT License.

---

# Support

If you like this project, consider giving it a star ⭐
