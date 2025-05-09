from flask import Flask, request, render_template
from SDTTranslator import SDTTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_code = ""
    if request.method == "POST":
        algorithm_text = request.form["algorithm"]
        translator = SDTTranslator()
        algorithm_lines = algorithm_text.splitlines()
        translated_code = translator.translate_algorithm(algorithm_lines)
    return render_template("index.html", translated_code=translated_code)

if __name__ == "__main__":
    porttt=8084
    app.run(debug=True, port=porttt)
   
