from flask import Blueprint, jsonify, Response
from .services import addition, subtraction, multiplication, division, modulus

calculator = Blueprint("calculator", __name__)


@calculator.route("/add/<int:a>/<int:b>", methods=["GET"])
def add_route(a: int, b: int) -> Response:
    result: int = addition(a, b)
    return jsonify({"result": result})


@calculator.route("/subtract/<int:a>/<int:b>", methods=["GET"])
def subtract_route(a: int, b: int) -> Response:
    result: int = subtraction(a, b)
    return jsonify({"result": result})


@calculator.route("/multiply/<int:a>/<int:b>", methods=["GET"])
def multiply_route(a: int, b: int) -> Response:
    result: int = multiplication(a, b)
    return jsonify({"result": result})


@calculator.route("/divide/<int:a>/<int:b>", methods=["GET"])
def divide_route(a: int, b: int) -> Response:
    result: float = division(a, b)
    return jsonify({"result": result})


@calculator.route("/modulus/<int:a>/<int:b>", methods=["GET"])
def modulus_route(a: int, b: int) -> Response:
    result: int = modulus(a, b)
    return jsonify({"result": result})
