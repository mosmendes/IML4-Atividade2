import pytest
from pydantic import ValidationError
from src.schemas.water_schema import WaterQualitySchema # Ajustado aqui

def test_water_schema_validation():
    # Dados válidos
    valid_data = {
        "ph": 7.0, "Hardness": 200.0, "Solids": 20000.0,
        "Chloramines": 7.0, "Sulfate": 300.0, "Conductivity": 400.0,
        "Organic_carbon": 10.0, "Trihalomethanes": 60.0, "Turbidity": 4.0
    }
    assert WaterQualitySchema(**valid_data)

def test_water_schema_invalid_data():
    # Dados inválidos (ph como string)
    invalid_data = {"ph": "muito_alto", "Hardness": 200.0}
    with pytest.raises(ValidationError):
        WaterQualitySchema(**invalid_data)