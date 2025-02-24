#---------------------------------------------------------------
#  PÁGINA UTLIZADA EM APLICAÇÃO DASH (app.py)
#  Monta e Exibe Graficos
#---------------------------------------------------------------

# Imports

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import seaborn as sns

# Carrega os dados
caracteristicas = pd.read_csv('./dados/dados_para_modelo.csv')

#----------------------------------------------------------------------
# GRAFICO1
#----------------------------------------------------------------------

grafico1 = px.histogram(caracteristicas, x='age')
grafico1.update_layout(
    title = {
        'text': 'Distribuição das Idades',
        'font': {'weight': 'bold'},
        'xanchor': 'left'
    },
    xaxis_title='Idades',
    yaxis_title='Frequência (303 amostras)',
)
grafico1.update_traces(marker=dict(line=dict(color='black', width=1)))
div_grafico1 = html.Div([
    dcc.Graph(figure = grafico1),
])


#----------------------------------------------------------------------
# GRAFICO2
#----------------------------------------------------------------------

grafico2 = px.histogram(caracteristicas, x='trestbps')
grafico2.update_layout(
    title = {
        'text': 'Distribuição da Pressão Arterial Máxima',
        'font': {'weight': 'bold'},
        'xanchor': 'left'
    },
    xaxis_title="Pressão Arterial Máxima",
    yaxis_title="Frequência (303 amostras)",
)
grafico2.update_traces(marker=dict(line=dict(color="black", width=1)))
grafico2.update_traces(marker=dict(color='green'))
div_grafico2 = html.Div([
    dcc.Graph(figure = grafico2),
])


#----------------------------------------------------------------------
# GRAFICO3
#----------------------------------------------------------------------

grafico3 = px.histogram(caracteristicas, x='chol')
grafico3.update_layout(
    title = {
        'text': 'Distribuição do Colesterol',
        'font': {'weight': 'bold'},
        'xanchor': 'left'
    },
    xaxis_title="Nível de Colesterol no Sangue (mg/dl)",
    yaxis_title="Frequência (303 amostras)",
)
grafico3.update_traces(marker=dict(line=dict(color="black", width=1)))
grafico3.update_traces(marker=dict(color='#FF5733'))
div_grafico3 = html.Div([
    dcc.Graph(figure = grafico3),
])


#----------------------------------------------------------------------
# GRAFICO4
#----------------------------------------------------------------------

# Agrupa por idade e calcula a média da pressão arterial
media_pressao_por_idade = caracteristicas.groupby('age')['trestbps'].mean().reset_index()

grafico4 = px.bar(media_pressao_por_idade,
             x='trestbps', 
             y='age', 
             labels={"trestbps": "Média da Pressão Arterial", "age": "Idade"})
grafico4.update_traces(marker=dict(line=dict(color="blue", width=1)))
grafico4.update_layout(
    title = {
        'text': 'Média da Pressão Arterial por Idade',
        'font': {'weight': 'bold'},
        'xanchor': 'left'
    },
    xaxis_title="Média da Pressão Arterial",
    yaxis_title="Idades",
)
div_grafico4 = html.Div([
    dcc.Graph(figure = grafico4),
])


#----------------------------------------------------------------------
# GRAFICO5
#----------------------------------------------------------------------

# Agrupa por sexo e calcula a média da pressão arterial
media_pressao_por_sexo = caracteristicas.groupby('sex', observed=False)['trestbps'].mean().reset_index()

# Converte a coluna 'sex' para o tipo categórico (se necessário)
media_pressao_por_sexo['sex'] = media_pressao_por_sexo['sex'].astype('category')

# Mapeia cores para 'sex' usando um dicionário
cor_map = {0: '#C435CF', 1: '#0013A6'}

grafico5 = px.bar(media_pressao_por_sexo, 
             x='sex', 
             y='trestbps', 
             title="Média da Pressão Arterial por Sexo",
             labels={"trestbps": "Média da Pressão Arterial", "sex": "Sexo"},
             color='sex',
             color_discrete_map=cor_map
)

grafico5.update_layout(
    xaxis_title="",
    yaxis_title="Média da Pressão Arterial",
    title_font=dict(weight='bold'),
    width=600,
    height=400,
    showlegend=False,
    xaxis=dict(showticklabels=False),
annotations=[
    dict(
        x=0.2, y=-0.22, 
        xref="paper", yref="paper", 
        text="Feminino                                     Masculino", 
        showarrow=False, 
        font=dict(size=12),
        align="left"
    )
]
)
div_grafico5 = html.Div([
    dcc.Graph(figure = grafico5),
])


#----------------------------------------------------------------------
# GRAFICO6
#----------------------------------------------------------------------

caracteristicas["doenca"] = (caracteristicas["doenca"] > 0) * 1

grafico6 = px.box(caracteristicas, x="doenca", y="age", color="doenca",
                  labels={"doenca": "Diagnósticos (0 = SEM Doença, 1 = COM Doença)", "age": "Idades"},
                  title="Relação Diagnósticos x Idades")
grafico6.update_layout(
    title={'text': 'Relação Diagnósticos x Idades', 'font': {'weight': 'bold'}, 'xanchor': 'left'},
    showlegend=False,
    height=400,
)
div_grafico6 = html.Div([
    dcc.Graph(figure = grafico6),
])


#----------------------------------------------------------------------
# Rodape
#----------------------------------------------------------------------

div_rodape = html.Div([
    html.P('Ayit Digital - Ciência de Dados e IA - Direitos Reservados - 2025', className='rodape'),
])


#---------------------------------------------------------------------------------
#  Trecho Principal - Montagem da Tela
#---------------------------------------------------------------------------------

layout = html.Div([
    html.Br(),
    html.H4('Análise dos Dados da UCI Repository Heart Disease (Doenças Cardíacas)', className='custom-title1'),
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.Col([div_grafico1], md=6),
            dbc.Col([div_grafico2], md=6),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([div_grafico3], md=6),
            dbc.Col([div_grafico4], md=6),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([div_grafico5], md=6),
            dbc.Col([div_grafico6], md=6),
        ]),
        html.Br(),
        html.Br(),
        div_rodape
    ])
])
