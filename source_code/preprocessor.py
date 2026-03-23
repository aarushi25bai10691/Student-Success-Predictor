import pandas as pd

def clean_input(study_hours, attendance):
    """Validates and formats the user input."""
    try:
        hr = float(study_hours)
        att = float(attendance)
        
        if not (0 <= hr <= 168): # Max hours in a week
            return None, "Invalid Study Hours (0-168)"
        if not (0 <= att <= 100):
            return None, "Invalid Attendance % (0-100)"
            
        return (hr, att), None
    except ValueError:
        return None, "Please enter numeric values."

def get_base_data():
    """Returns a simple training dataset."""
    data = {
        'Study_Hours': [10, 2, 8, 1, 7, 3, 9, 4, 12, 5],
        'Attendance': [90, 40, 85, 30, 80, 50, 95, 60, 98, 70],
        'Passed': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1] 
    }
    return pd.DataFrame(data)
