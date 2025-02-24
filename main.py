#---------------------------------------------------------------
#  APLICAÇÃO DASH - (Criação de Dashboard - Doenças Cardíacas)
#---------------------------------------------------------------

# Dashboard dinâmico e interativo utilizando a biblioteca Dash.
# Dash é uma ferramenta incrivelmente poderosa e flexível, projetada especificamente para pessoas que desejam construir 
# interfaces de usuário interativas para visualização de dados na web.
# 
# O Dash apresenta três pilares tecnológicos essenciais:
# 
# Flask: é um micro-framework para desenvolvimento web em Python.
# Quando você cria um dashboard com Dash, por baixo dos panos, ela está utilizando o Flask para lidar com as comunicações
# entre o navegador do usuário (cliente) e o servidor onde o aplicativo está rodando.
# Isso inclui receber pedidos do navegador, como quando interagimos com um componente da Dash, e enviar as respostas 
# apropriadas do servidor de volta ao navegador, permitindo assim a interatividade e a atualização dos componentes do aplicativo.
#
# Plotly.js: é uma biblioteca de gráficos JavaScript de código aberto que a Dash utiliza para renderizar visualizações de dados interativas.
#
# React: é uma biblioteca JavaScript para construir interfaces de usuário.
# Dash utiliza React.js para renderizar os componentes do lado do cliente. 
# Cada componente da Dash é essencialmente um componente React que pode ser interativo e dinâmico.
#
# Para obter mais informações sobre Dash, visite o repositório oficial no GitHub e consulte a documentação abrangente disponível no site da biblioteca.
# Além disso, você pode explorar diversos exemplos de dashboards criados com Dash na seção de exemplos do site.


# ESSA APLICAÇÃO TEM A SEGUINTE ESTRUTURA :
# main.py        -  O programa principal Python
# app.py         -  Criação (instancia) de aplicação Dash
# graficos.py    -  Pagina com Graficos
# formularios.py -  Pagina com o formulario que coleta dados e faz previsão com o modelo
# inicial.py     -  Pagina Inicial

# Essa estrutura é para que as páginas que tem callback conheçam o app

#  Material de Colsulta para o Bootstrap
#  https://dash-bootstrap-components.opensource.faculty.ai/docs/                  -   Documentação
#  https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/           -   Temas
#  https://dash-bootstrap-components.opensource.faculty.ai/docs/components/       -   Componentes


# Imports

# Importa o app que cria a aplicação Dash
from app import app

# Importa as paginas

import paginas.formulario
import paginas.graficos
import paginas.inicial

# Importa pacotes utlizados
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


# Define o trecho navegação

navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicial", href="/inicial")),
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
    ],
    brand=html.Div(
        children=[
            html.Img(src='/assets/logoayit.png', height='50px'),
            'Dashboard de Informações - Doenças Cardíacas'
        ],
        style={
            'font-size' : '28px',
            'display': 'flex',
            'alignItems': 'center', # Alinha os itens verticalmente ao centro
            'gap': '30px'           # Espaço entre a imagem e o texto
        }
    ),
    brand_href="#",
    color="primary",
    dark=True,
)


# Define o layout da página

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navegacao,
    html.Div(id='conteudo')
])


# Define o callback da ação das opções do menu 
# para chamada da página correspondente

@app.callback(
    Output('conteudo', 'children'),
    [Input('url','pathname')]
)
def mostrar_pagina(pathname):
    if pathname == '/formulario':
        return paginas.formulario.layout
    elif pathname == '/graficos':
        return paginas.graficos.layout
    else:
        return paginas.inicial.layout


# Início - Inicia o Servidor FLASK e a aplicação Dash

app.run_server(debug=True)
