# scripts/evaluate.py
import pickle
import json

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

metrics = {
    'average_marks': model['avg_marks'],
    'status': 'OK'
}

with open('results/metrics.json', 'w') as f:
    json.dump(metrics, f)

print("✅ Evaluation saved.")
