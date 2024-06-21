from flask import Blueprint, jsonify, Response
from datetime import datetime
from .services import addition, subtraction, multiplication, division, modulus
from .types import NumericType

calculator = Blueprint("calculator", __name__)


@calculator.route("/add/<int:a>/<int:b>", methods=["GET"])
def add_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = addition(a, b)
        response_time = datetime.now().isoformat()
        return (
            jsonify(
                {
                    "result": result,
                    "time_of_response": response_time,
                    "numbers_received": {"a": a, "b": b},
                    "operation": "addition",
                    "status": "success",
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e), "status": "error", "code": 400}), 400
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An unexpected error occurred",
                    "status": "error",
                    "code": 500,
                }
            ),
            500,
        )


@calculator.route("/subtract/<int:a>/<int:b>", methods=["GET"])
def subtract_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = subtraction(a, b)
        response_time = datetime.now().isoformat()
        return (
            jsonify(
                {
                    "result": result,
                    "time_of_response": response_time,
                    "numbers_received": {"a": a, "b": b},
                    "operation": "subtraction",
                    "status": "success",
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e), "status": "error", "code": 400}), 400
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An unexpected error occurred",
                    "status": "error",
                    "code": 500,
                }
            ),
            500,
        )


@calculator.route("/multiply/<int:a>/<int:b>", methods=["GET"])
def multiply_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = multiplication(a, b)
        response_time = datetime.now().isoformat()
        return (
            jsonify(
                {
                    "result": result,
                    "time_of_response": response_time,
                    "numbers_received": {"a": a, "b": b},
                    "operation": "multiplication",
                    "status": "success",
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e), "status": "error", "code": 400}), 400
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An unexpected error occurred",
                    "status": "error",
                    "code": 500,
                }
            ),
            500,
        )


@calculator.route("/divide/<int:a>/<int:b>", methods=["GET"])
def divide_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: float = division(a, b)
        response_time = datetime.now().isoformat()
        return (
            jsonify(
                {
                    "result": result,
                    "time_of_response": response_time,
                    "numbers_received": {"a": a, "b": b},
                    "operation": "division",
                    "status": "success",
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e), "status": "error", "code": 400}), 400
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An unexpected error occurred",
                    "status": "error",
                    "code": 500,
                }
            ),
            500,
        )


@calculator.route("/modulus/<int:a>/<int:b>", methods=["GET"])
def modulus_route(a: NumericType, b: NumericType) -> Response:
    try:
        result: NumericType = modulus(a, b)
        response_time = datetime.now().isoformat()
        return (
            jsonify(
                {
                    "result": result,
                    "time_of_response": response_time,
                    "numbers_received": {"a": a, "b": b},
                    "operation": "modulus",
                    "status": "success",
                }
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"error": str(e), "status": "error", "code": 400}), 400
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An unexpected error occurred",
                    "status": "error",
                    "code": 500,
                }
            ),
            500,
        )


@calculator.app_errorhandler(404)
def route_not_found(e):
    try:
        return (
            jsonify({"error": "Resource not found", "status": "error", "code": 404}),
            404,
        )
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An error occurred while handling your request",
                    "status": "error",
                    "code": 500,
                }
            ),
            500,
        )
