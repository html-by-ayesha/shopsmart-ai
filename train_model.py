import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load Dataset
df = pd.read_csv('products.csv')

# Label Encoding
le_age = LabelEncoder()
le_budget = LabelEncoder()
le_gender = LabelEncoder()
le_interest = LabelEncoder()
le_product = LabelEncoder()

df['Age'] = le_age.fit_transform(df['Age'])
df['Budget'] = le_budget.fit_transform(df['Budget'])
df['Gender'] = le_gender.fit_transform(df['Gender'])
df['Interest'] = le_interest.fit_transform(df['Interest'])
df['Product'] = le_product.fit_transform(df['Product'])

# Features & Target
x = df[['Age', 'Budget', 'Gender', 'Interest']]
y = df['Product']

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Gaussian Naive Bayes Model
model = GaussianNB()
model.fit(x_train, y_train)

# Accuracy
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc * 100:.2f}%")

# Save Model & Encoders
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(le_age, open('le_age.pkl', 'wb'))
pickle.dump(le_budget, open('le_budget.pkl', 'wb'))
pickle.dump(le_gender, open('le_gender.pkl', 'wb'))
pickle.dump(le_interest, open('le_interest.pkl', 'wb'))
pickle.dump(le_product, open('le_product.pkl', 'wb'))

print("✅ Model saved successfully!")
print("\n📦 Products in dataset:")
print(le_product.classes_)