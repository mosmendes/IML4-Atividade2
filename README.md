# 💧 Classificação de Potabilidade de Água

Este projeto foi desenvolvido como parte da disciplina IML4 do MBA em Ciência de Dados (UFSCar - 2025). O objetivo é construir um pipeline de Machine Learning robusto para classificar se a água é potável ou não, baseado em métricas físico-químicas.

## 🚀 Tecnologias e Boas Práticas
Para este projeto, foram implementadas as seguintes tecnologias e conceitos de MLOps:
- **Gerenciamento de Dependências:** [Poetry](https://python-poetry.org/)
- **Versionamento de Código e Dados:** Git e Bump2version
- **Experiment Tracking:** [MLflow](https://mlflow.org/) (usando banco de dados local SQLite)
- **Design Patterns:** Implementação do **Strategy Pattern** no script de treinamento.
- **Validação de Dados:** [Pydantic](https://docs.pydantic.dev/) para garantir integridade dos schemas.
- **Qualidade de Código:** Linting e formatação automatizada com **Ruff**.
- **Automação:** Makefile para facilitar a execução de comandos.

---

## 📁 Estrutura do Projeto
```text
├── data/               # Conjunto de dados (CSV)
├── src/
│   ├── data/          # Scripts de processamento e limpeza
│   ├── models/        # Lógica de treinamento (Strategy Pattern)
│   ├── schemas/       # Validação de dados (Pydantic)
│   └── utils/         # Funções auxiliares
├── Makefile           # Automação de tarefas
├── mlflow.db          # Banco de dados de experimentos
├── pyproject.toml     # Configurações do Poetry e dependências
└── README.md          # Documentação do projeto