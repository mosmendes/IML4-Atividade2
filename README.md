# Classificação de Potabilidade de Água

Este projeto foi desenvolvido como parte da disciplina IML4 do MBA em Ciência de Dados (UFSCar). O objetivo é construir um pipeline de Machine Learning robusto para classificar se a água é potável ou não, baseado em métricas físico-químicas.

---

## Tecnologias e Boas Práticas
Para este projeto, foram implementadas as seguintes tecnologias e conceitos de MLOps:
- **Gerenciamento de Dependências:** [Poetry](https://python-poetry.org/) para ambientes isolados e reprodutíveis.
- **CI/CD:** [GitHub Actions](https://github.com/features/actions) executando testes unitários automatizados em cada push.
- **Conteinerização:** [Docker](https://www.docker.com/) para portabilidade total da aplicação.
- **Experiment Tracking:** [MLflow](https://mlflow.org/) (usando banco de dados local SQLite) para registro de métricas e modelos.
- **Design Patterns:** Implementação do **Strategy Pattern** no script de treinamento.
- **Validação de Dados:** [Pydantic](https://docs.pydantic.dev/) para garantir a integridade dos schemas de entrada.
- **Qualidade de Código:** Linting e formatação automatizada com **Ruff**.

---

## Como Utilizar a Ferramenta

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.11+** e o **Poetry** instalados. Caso prefira utilizar via container, o **Docker Desktop** deve estar instalado e rodando.

### 2. Instalação Local
```powershell
poetry install
```

### 3. Execução dos Testes Unitários
O projeto possui testes que validam o processamento dos dados e a integridade dos schemas de entrada:
```powershell
$env:PYTHONPATH = "."; poetry run pytest
```

### 4. Treinamento e Registro do Modelo
O treinamento utiliza o MLflow para gerenciar o experimento. Para treinar o modelo:
```powershell
$env:PYTHONPATH = "."; poetry run python src/models/train.py
```

### 5. Execução da Inferência (Predição)
Para testar o modelo carregando-o diretamente do MLflow Model Registry com dados de exemplo:
```powershell
$env:PYTHONPATH = "."; poetry run python src/models/predict.py
```

## Utilizando o Docker
A ferramenta está pronta para ser executada em qualquer ambiente via container, garantindo que as versões das bibliotecas sejam idênticas às do desenvolvimento:

### 1. Construir a imagem
Construir a imagem:
```powershell
docker build -t water-potability-app .
```

### 2. Executar o container (Roda o script de predição automaticamente):
```powershell
docker run water-potability-app
```

## Estrutura do Projeto

```text
├── .github/workflows/  # Pipeline de Integração Contínua (CI)
├── data/               # Conjunto de dados original (CSV)
├── src/
│   ├── data/          # Scripts de processamento e limpeza
│   ├── models/        # Treinamento (Strategy) e Inferência (Predict)
│   ├── schemas/       # Validação de dados (Pydantic)
│   └── utils/         # Funções auxiliares
├── tests/              # Testes unitários para Pytest
├── Dockerfile          # Receita para construção da imagem Docker
├── Makefile            # Automação de comandos frequentes
├── mlflow.db           # Banco de dados de experimentos (SQLite)
├── mlruns/             # Modelos e métricas versionados
└── pyproject.toml      # Configuração de dependências do Poetry
```
