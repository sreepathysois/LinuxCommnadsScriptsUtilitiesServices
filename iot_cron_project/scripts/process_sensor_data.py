import pandas as pd
import glob
import json
import os

latest_file = sorted(glob.glob("data/sensor_*.csv"))[-1]
df = pd.read_csv(latest_file)

summary = {
    "file": latest_file,
    "average_temp": df["temperature"].mean(),
    "max_temp": df["temperature"].max(),
    "min_temp": df["temperature"].min(),
    "sensor_with_max": int(df.loc[df['temperature'].idxmax()]['sensor_id']),
}

os.makedirs("output", exist_ok=True)
with open("output/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print(f"📊 Summary: {summary}")
