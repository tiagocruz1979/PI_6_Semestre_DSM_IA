import os
import datetime
import holidays

from app.service.atualiza_data_service import atualizar_fundamentos


def buscarTicker(ticker=""):
    # verifica se o arquivo está desatualizado e atualizada
    atualizar_se_necessario()

    with open("./app/data/db_fundamentos.txt", "r") as file:
        cabecalho = next(file)

        colunasCabecalho = cabecalho.strip().split()

        linha_dict = {}

        for linha in file:
            colunas = linha.strip().split()

            nomeTicker = colunas[0]

            if nomeTicker == ticker:
                for i, coluna in enumerate(colunas):
                    linha_dict[colunasCabecalho[i]] = coluna

                return linha_dict

    return None


def obter_data_modificacao_arquivo():
    data_modificacao = os.path.getmtime("./app/data/db_fundamentos.txt")
    return datetime.datetime.fromtimestamp(data_modificacao).date()


def verificar_dia_util(data):
    # Verifica se a data não é sábado, domingo ou feriado nacional.
    if data.weekday() in [5, 6]:  # 5 é sábado, 6 é domingo
        return False

    br_holidays = holidays.Brazil()
    if data in br_holidays:
        return False

    return True


def atualizar_se_necessario():
    data_modificacao = obter_data_modificacao_arquivo()
    data_atual = datetime.datetime.now().date()

    # atualiza se o arquivo não for de hoje e se hoje for dia util
    if data_modificacao < data_atual and verificar_dia_util(data_atual):
        print("Atualizando o arquivo...")
        atualizar_fundamentos()
    else:
        print("Nenhuma atualização necessária.")
