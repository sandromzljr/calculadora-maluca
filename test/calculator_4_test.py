import sys

sys.path.append(".")

from typing import Dict, List
from pytest import raises
from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler():
    def mean(self, numbers: List[float]) -> float:
        return 3

def test_calculate():
    mock_request = MockRequest( {"numbers": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert isinstance(response, Dict)
    assert response == {"data": {"Calculator": 4, "mean": 3}}

def test_calculate_with_body_error():
    mock_request = MockRequest( {"numberssss": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "BODY MAL FORMATADO"

def test_calculate_with_empty_body_error():
    mock_request = MockRequest( {"numbers": [] })
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "NÃO FOI POSSÍVEL CALCULA A MÉDIA"
