from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        voltaje = float(request.form["voltaje"])
        potencia = float(request.form["potencia"])
        fp = float(request.form["fp"])

        corriente = potencia / (voltaje * fp)

        resultado = round(corriente, 2)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)