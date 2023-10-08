from flask import Flask, jsonify, request
from ia.iaTraining import fazer_previsao
from webScrap import extract_elements_for_anchor
from joblib import load
from flask_cors import CORS
import mysql.connector

app = Flask(_name_)
CORS(app)

# Defina a rota da API
@app.route('/api/extract_data/<anchor>', methods=['GET'])
def get_data(anchor):
    base_url = "https://www.usgs.gov/science/science-explorer/climate"
    
    elements = extract_elements_for_anchor(base_url, anchor)
    
    if elements is not None:
        return jsonify(elements)
    else:
        return jsonify({'error': 'Failed to retrieve data for anchor'}), 500


@app.route('/api/consultar', methods=['POST'])
def consultar():
    modelo_categoria = load('modelo_categoria.joblib')
    modelo_agencia = load('modelo_agencia.joblib')
    modelo_topico = load('modelo_topico.joblib')
    vetorizador = load('vetorizador.joblib')

    consulta = request.json.get('consulta')

    if consulta is None:
        return jsonify({'error': 'Consulta ausente'}), 400

    categoria_predita, agencia_predita, topico_predito = fazer_previsao(consulta)

    resposta = {
        'categoria_predita': categoria_predita[0],
        'agencia_predita': agencia_predita[0],
        'topico_predito': topico_predito[0]
    }

    
    
    return jsonify(resposta)


@app.route('/artigos', methods=['GET'])
def get_artigos():
    try:
        cnx = mysql.connector.connect(user='root', password='030696',
                                      host='127.0.0.1', port=3306,
                                      database='MeuBancoDeDados')
        cursor = cnx.cursor()

        cursor.callproc('LerArtigos')

        data = []
        for result in cursor.stored_results():
            data.append(result.fetchall())

        cursor.close()
        cnx.close()

        app.logger.info("Resultado da procedure LerArtigos: %s", data)


        return jsonify(data)
    except Exception as e:
        return str(e), 500


if _name_ == '_main_':
    app.run(debug=True)