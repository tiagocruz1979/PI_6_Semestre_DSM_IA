from flask import request, jsonify

from app.service import knn_service
from app.service import fundamentos_service


def analise():
    data: dict = request.get_json()
    # o data precisa receber o nome do ticker para busca na base de dados
    print(data)
    print(data["ticker"])

    # precisa criar uma função que leia o arquivo da base de dados com os fundamentos e retorne as informações do ticker passado no parametro
    empresa = fundamentos_service.buscarTicker(data["ticker"])

    # pegar as infromaçoes retornadas da base e analisar com o knn
    classificacao = knn_service.knn_analise(empresa)

    return jsonify({"recomendacao": classificacao[0]})
