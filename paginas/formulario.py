#---------------------------------------------------------------
#  PÁGINA UTLIZADA EM APLICAÇÃO DASH (app.py)
#  Formulário e Utilização de Modelo de ML
#---------------------------------------------------------------

# Imports

from app import app
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np
import xgboost as xgb


# Carrega o modelo

modelo = joblib.load('./modelos/modelo_xgboost.pkl')

# Cria a página

formulario = dbc.Container([

    html.H3("Previsão de Doença Cardíaca", className='mt-3 custom-title1'),

    html.P('* ATENÇÃO * - Informe todos os dados para que o modelo possa oferecer uma análise mais precisa.', style={'fontWeight': 'bold'}, className='mt-2 custom-subtitle'),
                        
    dbc.Row([

        dbc.Col([

            dbc.CardGroup([
                dbc.Label("Idade", className='bold-label'),
                dbc.Input(id='idade', type='number', placeholder='Digite ou Selecione a Idade (0 a 120)', min=0, max=120),
            ], className='mb-3'),

            dbc.CardGroup([ 
                dbc.Label("Sexo Biológico", className='bold-label'),
                dbc.Select(id='sexo', options=[
                    {'label': 'Masculino', 'value': '1'},
                    {'label': 'Feminino', 'value': '0'}
                ] , placeholder='Selecione o Sexo'),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Tipo de Dor no Peito", className='bold-label'),
                dbc.Select(id='cp', options=[
                    {'label': 'Angina Típica (dor no peito)', 'value': '1'},
                    {'label': 'Angina Atípica (dor em outras partes do corpo)', 'value': '2'},
                    {'label': 'Não Angina (sem dor ou com dor muscular/digestiva)', 'value': '3'},
                    {'label': 'Angina Assintomática (sem dor e sem desconforto)', 'value': '4'}
                ], placeholder='Selecione o Tipo de Dor'),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Pressão Arterial em Repouso (Máxima)", className='bold-label'),
                dbc.Input(id='trestbps', type='number', placeholder='Digite ou Selecione a Pressão Arterial (Máxima) em Repouso (50 a 220)', min=50, max=220),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Colesterol Sérico", className='bold-label'),
                dbc.Input(id='chol', type='number', placeholder='Digite ou Selecione o Colesterol Sérico (60 a 600)', min=60, max=600),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Glicemia em Jejum (Menor ou Maior que 120 mg/dl)", className='bold-label'),
                dbc.Select(id='fbs', options=[
                    {'label': 'Menor que 120 mg/dl', 'value': '0'},
                    {'label': 'Maior que 120 mg/dl', 'value': '1'}
                ], placeholder='Selecione a Faixa'),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Eletrocardiografia em Repouso", className='bold-label'),
                dbc.Select(id='restecg', options=[
                    {'label': 'Normal', 'value': '0'},
                    {'label': 'Anormalidades de ST-T', 'value': '1'},
                    {'label': 'Hipertrofia Ventricular Esquerda', 'value': '2'}
                ], placeholder='Selecione o Tipo de Resultado'),
            ], className='mb-3'),
        ]),

        dbc.Col([

            dbc.CardGroup([
                dbc.Label("Frequência Cardíaca Máxima Atingida", className='bold-label'),
                dbc.Input(id='thalach', type='number', placeholder='Digite ou Selecione a Frequência Cardíaca Máxima Atingida (60 a 250)', min=60, max=250),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Angina Induzida por Exercício", className='bold-label'),
                dbc.Select(id='exang', options=[
                    {'label': 'Sim', 'value': '1'},
                    {'label': 'Não', 'value': '0'}
                ], placeholder='Selecione Sim ou Não'),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Depressão do Segmento ST Induzida por Exercício", className='bold-label'),
                dbc.Input(id='oldpeak', type='number', placeholder='Digite ou Selecione a Depressão do Segmento ST Induzida por Exercício (0.0 a 9.9)', min=0.0, max=9.9, step=0.1),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Inclinação do Segmento ST", className='bold-label'),
                dbc.Select(id='slope', options=[
                    {'label': 'Ascendente', 'value': '1'},
                    {'label': 'Plana', 'value': '2'},
                    {'label': 'Descendente', 'value': '3'}
                ], placeholder='Selecione o Tipo de Inclinação'),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Número de Vasos Principais Coloridos por Fluoroscopia", className='bold-label'),
                dbc.Select(id='ca',
                    options = [
                        { 'label': '0', 'value': '0' },
                        { 'label': '1', 'value': '1' },
                        { 'label': '2', 'value': '2' },
                        { 'label': '3', 'value': '3' },
                    ], placeholder='Digite ou Selecione a Quantidade (0 a 3)'),
            ], className='mb-3'),

            dbc.CardGroup([
                dbc.Label("Cintilografia do Miocárdio", className='bold-label'),
                dbc.Select(id='thal', options=[
                    {'label': 'Normal', 'value': '3'},
                    {'label': 'Defeito Fixo', 'value': '6'},
                    {'label': 'Defeito Reversível', 'value': '7'}
                ], placeholder='Selecione o Tipo de Resultado'),
            ], className='mb-3'),

            dbc.Row([
                dbc.Col(
                    dbc.Button("Prever Existência de Doença Cardíaca",
                               id='botao-prever',
                               color='primary',
                               n_clicks=0,
                               style={'paddingLeft': '70px', 'paddingRight': '70px'}),
                    width="auto"
                ),
            ], justify="center", className='mt-5')
        ])
    ])
])       

# Pedaço : Rodapé

div_rodape = html.Div([
    html.P('Ayit Digital - Ciência de Dados e IA - Direitos Reservados - 2025', className='rodape'),
])

# Cria a página (layout e conteúdo)

layout = html.Div([
    formulario,
    html.Div(id='previsao'),
    div_rodape
])


# Definição da Função Para o Callback
@app.callback(
    Output('previsao', 'children'),
    [Input('botao-prever', 'n_clicks')],
    [State('idade', 'value'),
     State('sexo', 'value'),
     State('cp', 'value'),
     State('trestbps', 'value'),
     State('chol', 'value'),
     State('fbs', 'value'),
     State('restecg', 'value'),
     State('thalach', 'value'),
     State('exang', 'value'),
     State('oldpeak', 'value'),
     State('slope', 'value'),
     State('ca', 'value'),
     State('thal', 'value')
    ]
)
# Função 
def prever_doenca(n_clicks, idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):

    if n_clicks == 0:
        return ''
    
    entradas_usuario = pd.DataFrame(
        data = [[idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
        columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    )

    # Trata as entradas para verificar se todos os campos foram informados
    # A obrigatoriedade de todos os campos está relacionada aos requisitos
    # do modelo. Como não queremos definir nenhum conteudo inicial para os
    # campos, o usuário tera que informar todos!

    if (idade == None ):
        return responde('Idade Não Informada!')
        
    if (sexo == None):
        return responde('Sexo Não Informado')

    if (cp == None):
        return responde('Tipo de Dor no Peito Não Informada')

    if (trestbps == None ):
        return responde('Pressão Arterial (Máxima) em Repouso Não Informada')
        
    if (chol == None):
        return responde('Colesterol Sérico Não Informado')

    if (fbs == None):
        return responde('Glicemia de Jejum Não Informada')

    if (restecg == None ):
        return responde('Resultado do ECG Não Informado')
        
    if (thalach == None):
        return responde('Frequência Cardíaca Máxima Não Informada')

    if (exang == None):
        return responde('Andina Induzida Por Exercício Não Informada')

    if (oldpeak == None ):
        return responde('Depressão do Segmento ST Não Informada')
        
    if (slope == None):
        return responde('Inclinação do Segmento ST Não Informado')

    if (ca == None):
        return responde('Número de Vasos Principais Coloridos por Fluoroscopia Não Informado')

    if (thal == None):
        return responde('Cintilografia do Miocárdio Não Informada')

    # Converte string digitada em float (somente oldpeak)
    entradas_usuario['oldpeak'] = entradas_usuario['oldpeak'].astype(np.float64)

    # Converte strings digitadas em inteiros
    for col in entradas_usuario.columns:
        if col != 'oldpeak':
            entradas_usuario[col] = entradas_usuario[col].astype(int)

    # O XGBoost espera um DMatrix portanto é preciso converter DataFrame em um DMatrix
    entradas_usuario_dmatrix = xgb.DMatrix(entradas_usuario)

    # Faz a previsão
    previsao = modelo.predict(entradas_usuario_dmatrix)[0]

    # Definindo o limite
    limite = 0.5

    # Convertendo para 0 ou 1
    previsao_binaria = 1 if previsao >= limite else 0
    #print(f'Previsão Continua: {previsao}')
    #print(f'Previsão Binaria: {previsao_binaria}')
    
    # Apresenta Resultado 
    if previsao_binaria == 1:
        mensagem = "Com uma Acurácia de 80.33% - O modelo indica que o paciente provavelmente : TEM PROBLEMA CARDÍACO."
        cor_do_alerta = 'danger'
    else:
        mensagem = "Com uma Acurácia de 80.33% - O modelo indica que o paciente provavelmente : NÃO TEM PROBLEMA CARDÍACO."
        cor_do_alerta = 'light'
    alerta = dbc.Alert(mensagem, color=cor_do_alerta,
                       className='d-flex justify-content-center mb-5',
                       style={'width': '75%', 'margin': '0 auto'})
    return alerta


# Responde as mensagens de erro

def responde(msg_erro):
    alerta = dbc.Alert(msg_erro, color='danger',
                       className='d-flex justify-content-center mb-5', 
                       style={'width': '100%', 'margin' : '0 auto'})
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                alerta, 
                className='d-flex justify-content-center',
            )
        )
    )
