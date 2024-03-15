from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator4():
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        self.__verify_results(input_data)
        mean = self.__calculate_mean(input_data)

        formated_response = self.__format_response(mean)
        return formated_response

    def __validate_body(self, body: Dict) -> None:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("BODY MAL FORMATADO")

        input_data = body["numbers"]
        return input_data

    def __calculate_mean(self, numbers: List[float]) -> float:
        mean = self.__driver_handler.mean(numbers)
        return mean

    def __verify_results(self, mean: float) -> None:
        if not mean:
            raise HttpBadRequestError("NÃO FOI POSSÍVEL CALCULA A MÉDIA")

    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "mean": round(mean, 2)
            }
        }
