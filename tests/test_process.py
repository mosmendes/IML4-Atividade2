import pytest
import pandas as pd
import os
from src.data.process import prepare_data

def test_prepare_data_structure():
    # Cria um CSV temporário para teste
    path = "data/water_potability.csv"
    
    # Verifica se o arquivo existe antes de testar
    if os.path.exists(path):
        X_train, X_test, y_train, y_test = prepare_data(path)
        
        # Teste 1: Verifica se os dados foram divididos (X e y)
        assert len(X_train) > 0
        assert len(y_train) > 0
        
        # Teste 2: Verifica se não há valores nulos (seu process.py usa dropna)
        assert X_train.isnull().sum().sum() == 0
    else:
        pytest.skip("Dataset não encontrado para teste")