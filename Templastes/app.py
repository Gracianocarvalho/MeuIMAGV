from flask import Flask

IMAGV = Flask(__name__)

@IMAGV.route("/")
def index():
  return "Joshua"
def teste1():
    return "<p>Testando</p>"


IMAGV.add_url_rule("/teste","teste",teste1)

if __name__== "__main__":
    IMAGV.run(debug=True)