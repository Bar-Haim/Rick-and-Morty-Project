from flask import Flask, jsonify
from rm import rnm  # מייבאים את הפונקציה מהקובץ הקודם

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>הגעת לשרת של בר 🦸‍♀️</h1>
    <p>לצפייה בדמויות לחצי על הכפתור:</p>
    <a href="/characters">
        <button style="padding:10px;font-size:16px;">לדמויות</button>
    </a>
    """


@app.route("/characters")
def characters():
    return jsonify(rnm())  # משתמשים בפונקציה מהקובץ שלך

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
