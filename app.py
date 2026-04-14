from flask import Flask, render_template, request, jsonify
import socket
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    ip = data['ip']
    start = int(data['start'])
    end = int(data['end'])

    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), range(start, end+1))

    for port in results:
        if port:
            open_ports.append(port)

    return jsonify({"open_ports": open_ports})

if __name__ == '__main__':
    app.run(debug=True)