import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
df = pd.read_csv("spambase.data", header=None)

# Assign consistent column names
df.columns = [f"feature_{i}" for i in range(57)] + ["label"]

# Prepare training data
X = df.drop(columns=["label"])
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "spam_classifier.pkl")
print("✅ Model trained and saved as spam_classifier.pkl")
