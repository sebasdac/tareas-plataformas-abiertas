from flask import Flask, jsonify, request

app = Flask(__name__)


# 1. GET: obtener todos los estudiantes (datos de ejemplo).
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return jsonify({
        "mensaje": "Lista de estudiantes obtenida correctamente.",
        "estudiantes": ["Ana", "Carlos", "María"]
    })


# 2. POST: simular que se agrega un estudiante.
@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict) or not isinstance(datos.get("nombre"), str) or not datos["nombre"].strip():
        return jsonify({"mensaje": "Debe enviar un JSON con el nombre del estudiante."}), 400

    return jsonify({
        "mensaje": "Estudiante agregado correctamente.",
        "estudiante": datos["nombre"].strip()
    })


# 3. PUT: simular que se actualiza el estudiante del ID indicado.
@app.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict) or not isinstance(datos.get("nombre"), str) or not datos["nombre"].strip():
        return jsonify({"mensaje": "Debe enviar un JSON con el nuevo nombre del estudiante."}), 400

    return jsonify({
        "mensaje": "Estudiante actualizado correctamente.",
        "id": id
    })


# 4. DELETE: simular que se elimina el estudiante del ID indicado.
@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    return jsonify({
        "mensaje": "Estudiante eliminado correctamente.",
        "id": id
    })


if __name__ == '__main__':
    app.run(debug=True)
