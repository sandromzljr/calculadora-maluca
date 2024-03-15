import sys

sys.path.append(".")

from typing import Dict
from pytest import raises
from src.calculators.calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 3})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response.get("data")
    assert "result" in response.get("data")
    print(response)

    # Assertividade da Resposta
    assert response["data"]["result"] == 15.71
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"error": 3})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "BODY MAL FORMATADO!"
