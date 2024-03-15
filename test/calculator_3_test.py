import sys

sys.path.append(".")

from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError():
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriverHandler():
    def variance(self, numbers: List[float]) -> float:
        return 2147483648

def test_calculate_with_variance_error():
    mock_request = MockRequest( {"numbers": [1, 2, 3, 4, 5] })
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "FALHA NO PROCESSO, VARIÂNCIA MENOR QUE MULTIPLICAÇÃO"

def test_calculate():
    mock_request = MockRequest( {"numbers": [1, 1, 1, 1, 100] })
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)

    assert isinstance(response, Dict)
    assert response == {"data": {"Calculator": 3, "variance": 2147483648, "success": True}}
