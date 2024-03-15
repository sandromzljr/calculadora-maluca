from flask import Flask
from src.main.routes.calculators import calculators_route_bp

app = Flask(__name__)

app.register_blueprint(calculators_route_bp)
