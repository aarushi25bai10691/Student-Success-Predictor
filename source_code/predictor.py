from sklearn.tree import DecisionTreeClassifier
from preprocessor import get_base_data

class SuccessModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.train_model()

    def train_model(self):
        df = get_base_data()
        X = df[['Study_Hours', 'Attendance']]
        y = df['Passed']
        self.model.fit(X, y)

    def predict(self, hr, att):
        prediction = self.model.predict([[hr, att]])
        return prediction[0]
