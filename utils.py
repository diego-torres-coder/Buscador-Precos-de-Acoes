import pandas as pd

# Períodos que o usuário pode escolher
periodos = {
    '5 dias': '5d',
    '1 mês': '1mo',
    '6 meses': '6mo',
    '1 ano': '1y',
    '5 anos': '5y'
}


def obter_tickers():
    # Lê o CSV com os tickers de empresas listadas na B3
    df_tickers = pd.read_csv('acoes-listadas.csv', usecols=['Código'])

    # Ordena os tickers em ordem alfabética
    df_tickers.sort_values(by='Código', ascending=True, inplace=True)
    
    # Retorna uma lista com todos os tickers do arquivo
    return list(df_tickers['Código'])
