import mlflow.sklearn
import mlflow # Adicione esta importação
import pandas as pd
from src.schemas.water_schema import WaterQualitySchema

def run_inference():
    # --- CONFIGURAÇÃO DO MLFLOW ---
    # Aponta para o seu arquivo de banco de dados local
    mlflow.set_tracking_uri("sqlite:///mlflow.db") 
    
    # 1. Dados de exemplo
    sample_data = {
        "ph": 7.5,
        "Hardness": 210.0,
        "Solids": 18000.0,
        "Chloramines": 6.5,
        "Sulfate": 310.0,
        "Conductivity": 420.0,
        "Organic_carbon": 12.0,
        "Trihalomethanes": 65.0,
        "Turbidity": 3.8
    }

    print("--- Iniciando Predição ---")
    
    # 2. Validação com o Pydantic
    validated_data = WaterQualitySchema(**sample_data)
    
    # 3. Carregar o modelo
    # Note que usamos a Versão 2 que você criou com sucesso anteriormente
    model_uri = "models:/ModeloAgua/2" 
    
    try:
        model = mlflow.sklearn.load_model(model_uri)
        
        # 4. Preparar dados
        input_df = pd.DataFrame([validated_data.model_dump()])
        
        # 5. Predição
        prediction = model.predict(input_df)
        resultado = "POTÁVEL" if prediction[0] == 1 else "NÃO POTÁVEL"
        
        print(f"Resultado para os dados fornecidos: {resultado}")
        
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        print("Dica: Verifique se o arquivo mlflow.db está na raiz do projeto.")

if __name__ == "__main__":
    run_inference()