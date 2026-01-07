# Usa uma imagem leve do Python
FROM python:3.11-slim

# Evita que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Copia os arquivos de configuração de dependências
COPY pyproject.toml poetry.lock ./

# Configura o Poetry para não criar ambientes virtuais dentro do container
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Copia o restante do código e o banco de dados
COPY src/ ./src/
COPY data/ ./data/
COPY mlflow.db ./mlflow.db
COPY mlruns/ ./mlruns/

# Comando padrão: roda o teste de predição ao iniciar
CMD ["python", "src/models/predict.py"]