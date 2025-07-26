# scripts/plot.py
import json
import matplotlib.pyplot as plt

with open('results/metrics.json') as f:
    metrics = json.load(f)

plt.bar(['Average'], [metrics['average_marks']])
plt.title("Student Average Marks")
plt.savefig('results/plot.png')
print("✅ Plot generated.")
