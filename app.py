# Importa o streamlit com o apelido st
import streamlit as st

# Importa o pandas com o apelido pd
import pandas as pd

# Importa o yahoo finance com o apelido yf
import yfinance as yf

# Importa o módulo locale
import locale

# Importa funções e variáveis do script utils
from utils import periodos, obter_tickers

# Define o idioma da aplicação para ser o português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Define a configuração da página
st.set_page_config(
     page_title="Preços de Ações",
     page_icon=":chart_with_upwards_trend:",
     layout="centered"
)

# Define um título para a página
st.title('Buscador de Preços de Ações')

# Cria um menu suspenso para o usuário escolher um ticker
ticker_escolhido = st.selectbox('Selecione uma ação:', options=obter_tickers())

# Define as opções de intervalo que o usuário pode escolher
opcoes_intervalo = ('5 dias', '1 mês', '6 meses', '1 ano', '5 anos')

# Armazena o período que o usuário escolheu
periodo = st.radio('Escolha um intervalo', options=opcoes_intervalo)

# Obtém informações sobre o ticker com a biblioteca Yahoo Finance
ticker = yf.Ticker(ticker=f'{ticker_escolhido}.SA')

# Cria três tabs com os títulos especificados
tab1, tab2, tab3 = st.tabs(['Fechamento', 'Volume', 'Resumo'])

# Conteúdo da primeira tab
with tab1:
    # Define o título da seção para plotar o gráfico com preços de fechamento 
    st.header('Preços de Fechamento da Ação')

    # Dataframe com os preços de fechamento da ação escolhida
    df_precos_fechamento = ticker.history(period=periodos[periodo]).Close

    # Plota um gráfico de linha com os preços de fechamento no período escolhido
    st.line_chart(df_precos_fechamento)

# Conteúdo da segunda tab
with tab2:
    # Define o título da seção para plotar o gráfico com os volumes negociados 
    st.header('Volume Negociado')

    # Dataframe com os volumes negociados no período
    volumes = ticker.history(period=periodos[periodo]).Volume

    # Plota um gráfico de linha com os volumes negociados no período escolhido
    st.line_chart(data=volumes)

# Conteúdo da terceira tab
with tab3:
    # Define o título da seção para exibir um dataframe com informações da ação no período
    st.header('Resumo')

    # Exibe um dataframe com informações da ação
    st.write(ticker.history(period=periodos[periodo]))