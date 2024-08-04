from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

def calcular_distancia(x1, y1, x2, y2):
    """Calcula la distancia entre dos puntos (x1, y1) y (x2, y2) en un plano cartesiano."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calcular_pendiente(x1, y1, x2, y2):
    """Calcula la pendiente de la línea que conecta dos puntos (x1, y1) y (x2, y2) en un plano cartesiano."""
    if x2 - x1 == 0:
        return None  # La pendiente es indefinida si x1 == x2
    return (y2 - y1) / (x2 - x1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    x1 = data['x1']
    y1 = data['y1']
    x2 = data['x2']
    y2 = data['y2']
    
    distancia = calcular_distancia(x1, y1, x2, y2)
    pendiente = calcular_pendiente(x1, y1, x2, y2)
    
    return jsonify({
        'distancia': distancia,
        'pendiente': pendiente
    })

if __name__ == '__main__':
    app.run(debug=True)
