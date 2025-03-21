 from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    os.system(f"ping -c 1 {ip}")
    return f"Pinging {ip}"

if __name__ == '__main__':
    app.run(debug=True)
