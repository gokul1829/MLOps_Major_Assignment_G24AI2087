# train.py
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np

def main():
    # load dataset
    data = fetch_olivetti_faces()
    X = data.data
    y = data.target

    # Split: 70% train, 30% test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    # Train Decision Tree
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Save model and optionally the test split for test.py
    joblib.dump({
        "model": clf,
        "X_test": X_test,
        "y_test": y_test
    }, "savedmodel.pth")

    print("Training complete. savedmodel.pth written.")

if __name__ == "__main__":
    main()
