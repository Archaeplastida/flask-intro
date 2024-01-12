from flask import Flask, request
import operations
app = Flask(__name__)

@app.route("/<operation>")
def evaluate(operation):
    a, b = int(request.args.get("a", 0)), int(request.args.get("b", 1))
    return str(eval(f"operations.{operation}")(a,b))

@app.route("/math/<operation>")
def evaluate2(operation):
    a, b = int(request.args.get("a", 0)), int(request.args.get("b", 1))
    return str(eval(f"operations.{operation}")(a,b))
