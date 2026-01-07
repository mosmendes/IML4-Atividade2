.PHONY: install train view-mlflow clean

install:
	poetry install
	poetry run pre-commit install

train:
	poetry run powershell -Command "$$env:PYTHONPATH='.'; poetry run python src/models/train.py"

view-mlflow:
	poetry run mlflow ui --backend-store-uri sqlite:///mlflow.db

clean:
	Remove-Item -Recurse -Force mlruns, mlflow.db, .venv -ErrorAction SilentlyContinue