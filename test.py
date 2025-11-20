# test.py
import joblib
from sklearn.metrics import accuracy_score

def main():
    saved = joblib.load("savedmodel.pth")
    clf = saved["model"]
    X_test = saved["X_test"]
    y_test = saved["y_test"]

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test Accuracy: {acc * 100:.2f}%")

if __name__ == "__main__":
    main()



