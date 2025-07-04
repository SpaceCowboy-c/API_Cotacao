from django.shortcuts import render
import requests  #requisições HTTP a APIs externas

def cotacao_view(request):

    moedas_api = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,THB-BRL'
    cripto_api = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=brl'

    try:
        moedas_resposta = requests.get(moedas_api).json()  #faz uma requisição para as apis e transforma eles em JSON (method GET)
        cripto_resposta = requests.get(cripto_api).json()

        moedas = {
            'Dólar (USD)': moedas_resposta['USDBRL']['bid'],  #criação de chaves: Nome + valor (bid)
            'Euro (EUR)': moedas_resposta['EURBRL']['bid'],
            'Baht Tailandês (THB)': moedas_resposta['THBBRL']['bid'],
        }

        criptos = { 
            'Bitcoin': cripto_resposta['bitcoin']['brl'],  #criação de chaves: Nome + valor (bid), (brl extrai para real)
            'Ethereum': cripto_resposta['ethereum']['brl'],
            'Solana': cripto_resposta['solana']['brl'],
        }

    except Exception:   #tratamento de erros
        moedas = {
            'Dólar (USD)': 'Erro',
            'Euro (EUR)': 'Erro',
            'Baht Tailandês (THB)': 'Erro',
        }
        criptos = {
            'Bitcoin': 'Erro',
            'Ethereum': 'Erro',
            'Solana': 'Erro',
        }

    return render(request, 'Cotacao.html', {'moedas': moedas, 'criptos': criptos})  #renderiza a tela passando esses dois parâmetros
