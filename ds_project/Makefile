.PHONY: all clean

all: results/plot.png

data/clean.csv: data/raw.csv
	python3 scripts/preprocess.py

models/model.pkl: data/clean.csv
	python3 scripts/train.py

results/metrics.json: models/model.pkl
	python3 scripts/evaluate.py

results/plot.png: results/metrics.json
	python3 scripts/plot.py

clean:
	rm -f data/clean.csv models/model.pkl results/*.*
