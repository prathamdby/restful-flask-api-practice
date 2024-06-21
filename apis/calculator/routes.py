from flask import Blueprint, jsonify, Response
from .services import addition, subtraction, multiplication, division, modulus
from .types import NumericType

calculator = Blueprint("calculator", __name__)


@calculator.route("/add/<int:a>/<int:b>", methods=["GET"])
def add_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = addition(a, b)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@calculator.route("/subtract/<a>/<b>", methods=["GET"])
def subtract_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = subtraction(a, b)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@calculator.route("/multiply/<a>/<b>", methods=["GET"])
def multiply_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = multiplication(a, b)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@calculator.route("/divide/<a>/<b>", methods=["GET"])
def divide_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: float = division(a, b)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@calculator.route("/modulus/<a>/<b>", methods=["GET"])
def modulus_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = modulus(a, b)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500


@calculator.app_errorhandler(404)
def route_not_found(e):
    try:
        return jsonify({"error": "Resource not found"}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred while handling your request"}), 500
