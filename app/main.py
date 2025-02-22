from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Scientific Calculator API!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get("operation")
    num1 = data.get("num1")
    num2 = data.get("num2", None)  # Some operations require only one number
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "square":
        result = num1 ** 2
    elif operation == "sqrt":
        result = math.sqrt(num1)
    elif operation == "power":
        result = math.pow(num1, num2)
    elif operation == "log":
        result = math.log(num1, num2) if num2 else math.log(num1)
    else:
        return jsonify({"error": "Invalid operation"}), 400
    
    return jsonify({"operation": operation, "result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
