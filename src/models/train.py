import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from src.data.process import prepare_data
from abc import ABC, abstractmethod

# --- REQUISITO: Design Pattern (Strategy) ---
class TrainingStrategy(ABC):
    @abstractmethod
    def execute(self, X_train, y_train):
        pass

class RandomForestStrategy(TrainingStrategy):
    def __init__(self, n_estimators=100, max_depth=5):
        self.params = {"n_estimators": n_estimators, "max_depth": max_depth}
        self.model = RandomForestClassifier(**self.params)

    def execute(self, X_train, y_train):
        return self.model.fit(X_train, y_train)

# --- Função Principal de Treino ---
def train():
    # Configura o MLflow
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("Agua_Potavel")

    # Prepara os dados
    X_train, X_test, y_train, y_test = prepare_data("data/water_potability.csv")

    with mlflow.start_run():
        # Instancia a estratégia (Design Pattern)
        strategy = RandomForestStrategy(n_estimators=100, max_depth=5)
        
        # Executa o treino
        model = strategy.execute(X_train, y_train)

        # Avaliação
        acc = model.score(X_test, y_test)

        # Tracking no MLflow
        mlflow.log_params(strategy.params)
        mlflow.log_metric("accuracy", acc)

        # Registro do Modelo
        mlflow.sklearn.log_model(model, "model", registered_model_name="ModeloAgua")
        print(f"Treino Finalizado com Strategy Pattern. Acurácia: {acc}")

if __name__ == "__main__":
    train()