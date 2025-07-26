# scripts/train.py
import pandas as pd
import pickle

df = pd.read_csv('data/clean.csv')
avg = df['Marks'].mean()

with open('models/model.pkl', 'wb') as f:
    pickle.dump({'avg_marks': avg}, f)

print(f"✅ Model trained. Average: {avg}")
