
import pandas as pd
from sklearn.metrics import accuracy_score
import importlib.util

def evaluate_submission(problem_id: str, submission_path: str):
    try:
        # Load user submission dynamically
        spec = importlib.util.spec_from_file_location("user_submission", submission_path)
        user_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user_module)

        # Load test data
        test_data = pd.read_csv(f"problems/{problem_id}/test.csv")
        X_test = test_data.drop("target", axis=1)
        y_true = test_data["target"]

        # Predict
        y_pred = user_module.predict(X_test)

        # Evaluate
        acc = accuracy_score(y_true, y_pred)
        return f"✅ Accuracy: {acc:.2%}"

    except Exception as e:
        return f"❌ Error: {str(e)}"
