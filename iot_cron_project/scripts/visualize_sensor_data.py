import pandas as pd
import matplotlib.pyplot as plt
import glob
from datetime import datetime
import os

latest_file = sorted(glob.glob("data/sensor_*.csv"))[-1]
df = pd.read_csv(latest_file)

plt.bar(df['sensor_id'].astype(str), df['temperature'], color='coral')
plt.title("Sensor Temperature Readings")
plt.xlabel("Sensor ID")
plt.ylabel("Temperature (°C)")
plt.tight_layout()

os.makedirs("output", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
plot_file = f"output/plot_{timestamp}.png"
plt.savefig(plot_file)
print(f"📈 Plot saved: {plot_file}")
