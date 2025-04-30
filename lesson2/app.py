from flask import Flask

app = Flask(__name__)

# Задание 1: Простые маршруты
@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/info")
def info():
    return "This is an informational page."

# Задание 2: Динамический маршрут для суммы чисел
@app.route("/calc/<a>/<b>")
def calc(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        return f"The sum of {num1} and {num2} is {num1 + num2}."
    except ValueError:
        return "Error: Both values must be integers."

# Задание 3: Переворот текста
@app.route("/reverse/<text>")
def reverse(text):
    if len(text) < 1:
        return "Error: Text must contain at least one character."
    return text[::-1]

# Задание 4: Приветствие с возрастом
@app.route("/user/<name>/<int:age>")
def user(name, age):
    if age < 0:
        return "Error: Age must be a non-negative number."
    return f"Hello, {name}. You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)
