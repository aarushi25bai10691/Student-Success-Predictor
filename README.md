# Student-Success-Predictor

# STUDENT SUCCESS PREDICTOR PROJECT 🎓
Submitted by: Aarushi Chauhan | 25BAI10691

# 📖 <u>PROJECT OVERVIEW</u>
This is a Python-based Machine Learning application developed as part of the Fundamentals of AI and ML course. It aims to tackle academic challenges by predicting whether a student is likely to "Pass" or is "At Risk" based on their study habits and engagement.

The project demonstrates the practical application of Supervised Learning, data preprocessing, and automated diagnostic feedback in an educational context.

# ✨ <u>FEATURES</u>
🚀 Success Prediction: Uses a Decision Tree algorithm to classify student outcomes with high precision.

📊 Data-Driven Insights: Analyzes key metrics such as Weekly Study Hours and Attendance Percentage.

💡 Smart Recommendations: Automatically generates tailored advice based on the prediction to help students improve.

💻 User-Friendly CLI: A <u>clean, menu-driven command-line interface</u> for seamless user interaction.

🏗️ Modular Architecture: Source code is organized into specific modules for training, prediction, and validation.

# 📂 <u>PROJECT STRUCTURE</u>
The project is organized for clarity and maintainability:

source_code/
main.py: The entry point script containing the application menu.

predictor.py: Core logic for loading the ML model and making inferences.

preprocessor.py: Handles data cleaning and ensures inputs are in the correct format.

recommender.py: Contains the logic for generating student improvement tips.

student_data.csv: Local database storing historical student records for training.

Root Files
statement.md: Contains the problem statement, project scope, target users, and features.

requirements.txt: List of dependencies required to run the project.

# 🛠️ <u>TECHNOLOGY STACK</u>
🐍 Language: Python 3

🧠 AI/ML Concepts: Modular Programming, Supervised Learning, Decision Trees, Data Validation.

📚 Libraries: Scikit-learn, Pandas, NumPy.

# 🚀 <u>STEPS TO INSTALL & RUN</u>
Clone the repository: git clone https://github.com/yourusername/student-success-predictor.git

Navigate to the source code directory: cd source_code

Run the application: python main.py

Follow the on-screen prompts to input student data and view AI predictions.

# ✔️ <u>INSTRUCTIONS FOR TESTING</u>
Test the application by entering these cases using Option 1 ("Predict Success"):

Case 1:

Study Hours: 15 | Attendance: 95% ➔ Result: ✅ Likely to PASS

Case 2:

Study Hours: 2 | Attendance: 40% ➔ Result: ⚠️ At RISK (Needs Improvement)

Case 3:

Study Hours: 8 | Attendance: 75% ➔ Result: ✅ Likely to PASS

Case 4:

Study Hours: 10 | Attendance: 20% ➔ Result: 🚩 At RISK (Attendance Warning)

Case 5:

Study Hours: 5 | Attendance: 65% ➔ Result: 🟠 Borderline (Action Required)

Use "View Model Accuracy" to see the performance report. Invalid input (wrong percentage or non-numeric hours) will trigger validation errors.

# 📸 <u>SCREENSHOTS</u>
(Screenshots are in the /assets directory to demonstrate the prediction flow, recommendation logic, and model performance metrics.)
