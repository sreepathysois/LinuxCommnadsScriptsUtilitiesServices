import pandas as pd
from datetime import datetime
import os
import random

os.makedirs("data", exist_ok=True)
date_str = datetime.now().strftime("%Y-%m-%d")

df = pd.DataFrame({
    "timestamp": [datetime.now().isoformat()] * 3,
    "sensor_id": [101, 102, 103],
    "temperature": [round(random.uniform(25, 35), 1) for _ in range(3)]
})

file_path = f"data/sensor_{date_str}.csv"
df.to_csv(file_path, index=False)
print(f"🛰 Data ingested: {file_path}")
