from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

def is_valid_ip(ip):
    # IP formatını kontrol eder
    return re.match(r'^[0-9\.]+$', ip) is not None

@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    if not ip or not is_valid_ip(ip):
        return jsonify({'error': 'Invalid IP address'}), 400

    try:
        # Güvenli şekilde ping komutu çalıştırılıyor
        result = subprocess.check_output(['ping', '-c', '4', ip], text=True)
        return f"<pre>{result}</pre>"
    except subprocess.CalledProcessError:
        return jsonify({'error': 'Ping failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
