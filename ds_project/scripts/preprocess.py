# scripts/preprocess.py
import pandas as pd
import sys

df = pd.read_csv('data/raw.csv')
df['Marks'] = df['Marks'] + 1  # simulate "cleaning"
df.to_csv('data/clean.csv', index=False)
print("✅ Preprocessing complete.")
