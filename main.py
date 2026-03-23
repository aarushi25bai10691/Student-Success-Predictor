import os
from predictor import SuccessModel
from preprocessor import clean_input
from recommender import get_advice

def show_menu():
    print("\n" + "="*35)
    print("  STUDENT SUCCESS PREDICTOR 🎓  ")
    print("="*35)
    print("1. Predict Success")
    print("2. View Project Info")
    print("3. Exit")
    print("="*35)

def main():
    ai_engine = SuccessModel()
    
    while True:
        show_menu()
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            hr = input("Enter Weekly Study Hours: ")
            att = input("Enter Attendance %: ")
            
            data, error = clean_input(hr, att)
            if error:
                print(f"❌ Error: {error}")
            else:
                res = ai_engine.predict(data[0], data[1])
                print(get_advice(res, data[0], data[1]))
                
        elif choice == '2':
            print("\n📖 Info: This AI uses a Decision Tree Classifier")
            print("to predict academic outcomes based on engagement.")
            
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
