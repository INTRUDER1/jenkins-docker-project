from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("calculator.html")  # Render the calculator UI

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
