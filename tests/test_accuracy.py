import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score

model = joblib.load("assets/model.joblib")
loans = pd.read_parquet("assets/loans_test.pqt")
label = "Repaid"
X = loans.drop(columns=label)
y = loans[label]
pred = model.predict(X)
probs = model.predict_proba(X)[:, 1]


def test_auc(json_metadata):
    auc = roc_auc_score(y, probs)
    assert 0.6 < auc < 0.7
    json_metadata["section"] = "Accuracy"
    json_metadata["pass_message"] = f"AUC is acceptable ({auc:.2f})"
    json_metadata["fail_message"] = f"AUC is inacceptable ({auc:.2f})"


def test_accuracy(json_metadata):
    accuracy = accuracy_score(y, pred)
    assert 0.8 < accuracy < 0.9
    json_metadata["section"] = "Accuracy"
    json_metadata["pass_message"] = f"Accuracy is acceptable ({accuracy:.2f})"
    json_metadata["fail_message"] = f"Accuracy is inacceptable ({accuracy:.2f})"
