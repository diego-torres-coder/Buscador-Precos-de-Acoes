# Buscador de Preços de Ações

Este projeto usa a biblioteca **Yahoo Finance** a fim de obter informações de um ativo listado na B3 (Bolsa de Valores Brasileira). O usuário escolhe o ticker em um menu suspenso e seleciona o período para o qual ele deseja obter informações.

Na captura de tela abaixo, o usuário escolheu o ticker PETR3 e deseja obter informações dos preços das ações para os últimos 6 meses:

![Captura de tela do buscador de preços de ações](/buscador-precos-acoes.png "Preços de fechamento do ativo PETR3")

## Como Reproduzir este Projeto

Em primeiro lugar, navegue até a pasta em que deseja clonar este projeto. Depois, digite o seguinte comando em seu terminal:

```bash
git clone https://github.com/diego-torres-coder/Buscador-Precos-de-Acoes.git
```

Pronto, você clonou o repositório deste projeto em sua máquina. Agora, navegue até a pasta do projeto:

```bash
cd Buscador-Precos-de-Acoes/
```

Crie um ambiente conda para o projeto, digitando o seguinte comando:

```bash
conda create -n stenv-precos-acoes python=3.10
```

Ative o ambiente com o seguinte comando:

```bash
conda activate stenv-precos-acoes
```

Com o ambiente ativo, instale as dependências do projeto:

```bash
pip install numpy openpyxl pandas yfinance streamlit
```

Alternativamente, você poderá instalar as dependências a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Por fim, execute a aplicação:

```bash
streamlit run app.py
```
