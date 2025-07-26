#!/bin/bash
cd /home/msis/iot_cron_project

echo "=== IoT Pipeline Started: $(date) ===" >> cron.log

python3 scripts/ingest_sensor_data.py >> cron.log 2>&1
python3 scripts/process_sensor_data.py >> cron.log 2>&1
python3 scripts/visualize_sensor_data.py >> cron.log 2>&1

echo "=== Pipeline Finished ===" >> cron.log
