from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test_route():
    return "Test route is working!"

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        data = {
            "message": "Hello, this is your data!",
            "status": "success",
            "data": {
                "id": 1,
                "name": "Sample Data",
                "description": "This is some sample data."
            }
        }
        return jsonify(data)
    
    elif request.method == 'POST':
        data = request.get_json()
        if data:
            response = {
                "message": "Data received successfully!",
                "status": "success",
                "received_data": data
            }
        else:
            response = {
                "message": "No data received",
                "status": "error"
            }
        return jsonify(response)

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error occurred!"}), 500

if __name__ == '__main__':
    app.run(debug=True)