from flask import Flask

app = Flask(__name__)


@app.route('/F2C/<int:value>')
def fahrenheit_to_celsius(value):
    result = str((value - 32) * 5 / 9)
    return "%sF = %sC" % (value, result)


@app.route('/C2F/<int:value>')
def celsius_to_fahrenheit(value):
    result = str((value * 9 / 5) + 32)
    return "%sC = %sF" % (value, result)


if __name__ == "__main__":
    app.run(debug=True)
