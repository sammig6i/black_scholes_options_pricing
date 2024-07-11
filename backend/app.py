from flask import Flask, jsonify
from black_scholes import BlackScholesModel

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def home():
  S = 100
  K = 100
  T = 1
  r = 0.05
  sigma = 0.02

  model = BlackScholesModel(S, K, T, r, sigma)

  put_price = model.calculate_put_price()
  call_price = model.calculate_call_price()

  return jsonify({
    'call_price': call_price,
    'put price': put_price
  })


if __name__ == "__main__":
  app.run(debug=True)