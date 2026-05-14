import pandas as pd
import pickle
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# ===============================
# 1. LOAD DATASET
# ===============================
df = pd.read_excel("dataset.xlsx")

# ===============================
# 2. SELECT FEATURES & TARGET
# ===============================
features = [
    "Mileage",
    "Quantity_Used",
    "Estimated_Usage_km",
    "Remaining_Life_km"
]

X = df[features]
y = df["Health_Status"]

# ===============================
# 3. ENCODE TARGET
# ===============================
le = LabelEncoder()
y = le.fit_transform(y)

# ===============================
# 4. TRAIN-TEST SPLIT
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ===============================
# 5. DEFINE MODELS
# ===============================
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(eval_metric="logloss"),
    "Naive Bayes": GaussianNB()
}

comparison_metrics = {}

# ===============================
# 6. TRAIN + EVALUATE ALL MODELS
# ===============================
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    comparison_metrics[name] = {
        "accuracy": round(accuracy_score(y_test, y_pred), 3),
        "precision": round(precision_score(y_test, y_pred), 3),
        "recall": round(recall_score(y_test, y_pred), 3),
        "f1_score": round(f1_score(y_test, y_pred), 3)
    }

    print(f"\n--- {name} ---")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("Report:")
    print(classification_report(y_test, y_pred))

# ===============================
# 7. SAVE FINAL MODEL (RF)
# ===============================
final_model = models["Random Forest"]
with open("model.pkl", "wb") as f:
    pickle.dump(final_model, f)

# ===============================
# 8. SAVE METRICS FOR DASHBOARD
# ===============================
with open("comparison_metrics.json", "w") as f:
    json.dump(comparison_metrics, f, indent=4)

# ===============================
# 9. SAVE LABEL MAPPING
# ===============================
with open("label_classes.json", "w") as f:
    json.dump(le.classes_.tolist(), f, indent=4)

print("\nmodel.pkl, comparison_metrics.json, and label_classes.json saved successfully!")