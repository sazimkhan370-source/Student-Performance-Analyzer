INTELLIGENT STUDENT PERFORMANCE ANALYZER
=========================================

PROJECT TECHNOLOGIES
- Python
- Flask
- HTML
- CSS
- scikit-learn (Decision Tree Machine Learning model)
- NumPy

HOW TO OPEN
1. Extract this ZIP file.
2. Open VS Code.
3. Select File > Open Folder.
4. Choose the extracted Student_Performance_Analyzer folder.

INSTALLATION
Open the VS Code terminal in the project folder and run:

    python -m pip install -r requirements.txt

RUN THE PROJECT
In the same terminal, run:

    python app.py

Open your browser and visit:

    http://127.0.0.1:5000

HOW TO USE
1. Enter a student name and roll number.
2. Enter marks from 0 to 100 in all five subjects.
3. Click Analyze Performance.
4. View the total, percentage, grade and predicted performance.
5. Click Analyze Another Student to try again.

IMPORTANT AI/MACHINE LEARNING NOTE
The project trains a Decision Tree classifier using generated example marks.
The labels are based on average marks:
- 80 or above: Excellent
- 60 to below 80: Good
- 40 to below 60: Average
- Below 40: Needs Improvement

This is an educational demonstration, not a validated real-world prediction
system. For a serious project, train and test the model on a suitable,
consented and representative student dataset.

TROUBLESHOOTING
- If 'pip' is not recognized, use:
      python -m pip install -r requirements.txt
- If the website does not open, check that app.py is still running.
- To stop the server, press Ctrl+C in the terminal.
