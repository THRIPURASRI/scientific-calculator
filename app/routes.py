from flask import Blueprint, render_template, request
from .calculator import evaluate_expression

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expr = request.form.get("expression")
        result = evaluate_expression(expr)
    return render_template("index.html", result=result)
