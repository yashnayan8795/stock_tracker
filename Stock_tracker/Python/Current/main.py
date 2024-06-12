from flask import request, render_template, jsonify, Flask
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json().get('ticker')
    try:
        data = yf.Ticker(ticker).history(period='1y')
        if data.empty:
            return jsonify({'error': 'Invalid ticker or no data available'}), 400
        return jsonify({
            'currentPrice': data.iloc[-1].Close,
            'openPrice': data.iloc[-1].Open
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
