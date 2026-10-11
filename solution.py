import datetime
import requests


def cotar():
    hoje = datetime.date.today()
    dias = [
        hoje - datetime.timedelta(days=i)
        for i in range(365)
    ]
    resultados = []

    url = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/"
        "versao/v1/odata/"
        "CotacaoDolarDia(dataCotacao=@dataCotacao)"
    )

    with requests.Session() as sessao:
        for dia in dias:
            parametros = {
                "@dataCotacao": f"'{dia.strftime('%m-%d-%Y')}'",
                "$format": "json",
                "$select": "cotacaoCompra",
            }

            resposta = sessao.get(
                url,
                params=parametros,
                timeout=30,
            )

            if resposta.status_code != 200:
                print("URL:", resposta.url)
                print("Mensagem do Banco Central:", resposta.text)

            resposta.raise_for_status()

            dados = resposta.json()["value"]
            compra = dados[0]["cotacaoCompra"] if dados else None

            resultados.append({
                "data": dia.isoformat(),
                "cotacaoCompra": compra,
            })

            if compra is None:
                print(f"{dia:%d/%m/%Y}: sem cotação")
            else:
                print(f"{dia:%d/%m/%Y}: R$ {compra:.4f}")

    return resultados