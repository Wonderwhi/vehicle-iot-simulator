from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    data_store.append(data)
    print(f"Received: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('', methods=['GET'])
def dashboard():
    html = """
    <html>
    <head>
        <title>Vehicle IoT Dashboard</title>
        <meta http-equiv="refresh" content="2">
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                background: #f4f4f4;
            }
            h1 {
                color: #222;
            }
            .card {
                background: white;
                padding: 15px;
                margin-bottom: 10px;
                border-radius: 10px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <h1>Vehicle IoT Dashboard</h1>
        <p>Total records: """ + str(len(data_store)) + """</p>
    """

    for item in reversed(data_store[-10:]):
        html += f"""
        <div class="card">
            <p><strong>Speed:</strong> {item.get('speed')}</p>
            <p><strong>Engine Temp:</strong> {item.get('engine_temp')}</p>
            <p><strong>Fuel Level:</strong> {item.get('fuel_level')}</p>
        </div>
        """

    html += """
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)