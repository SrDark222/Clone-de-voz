from flask import Flask, render_template, request, send_file
from selenium_bot.clone_script import gerar_audio
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texto = request.form["texto"]
        nome_voz = request.form["voz"]
        audio_path = gerar_audio(texto, nome_voz)
        return send_file(audio_path, as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
