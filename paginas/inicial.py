#---------------------------------------------------------------
#  PÁGINA UTLIZADA EM APLICAÇÃO DASH (app.py)
#  Pagina Inicial
#---------------------------------------------------------------

# Imports

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


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
    html.H3('UC Irvine - Universidade da California - Doenças Cardíacas', className = 'desloca-h'),
    html.Div([
        html.Br(),
        html.P('Os dados utilizados nesse projeto foram obtidos do UCI Machine Learning Repository.'),
        html.P('Esses dados provêm dos resultados clínicos e de testes não invasivos realizados em pacientes submetidos a exames'),
        html.P('na Cleveland Clinic em Cleveland (Ohio), no Instituto Húngaro de Cardiologia em Budapeste, em um Centro Médico em Long Beach (Califórnia)'), 
        html.P('e também em pacientes de Hospitais universitários em Zurique e Basel (Suíça).'),
        html.P('Inicialmente, o conjunto de dados continha 76 variáveis, mas todas as análises realizadas concentram-se no uso de um subconjunto de 14 delas.'),
        html.P('Vale destacar que, até o momento, o banco de dados da Cleveland Clinic é o único utilizado por pesquisadores de aprendizado de máquina.'),
        html.P('As análises realizadas com esse banco de dados tem como objetivo distinguir a presença da doença cardíaca (valor 1) da sua ausência (valor 0).'),
        html.P('As features do dataset que foram consideradas nesse projeto foram:'),
        html.P('- Idade em anos'),
        html.P('- Sexo'),
        html.P('- Tipo de dor no peito relatada pelo paciente'),
        html.P('- Pressão arterial medida em repouso'),
        html.P('- Nível de colesterol no sangue em miligramas por decilitro (mg/dl)'),
        html.P('- Nível de glicose no sangue em jejum'),
        html.P('- Resultado do eletrocardiograma em repouso'),
        html.P('- Frequência cardíaca máxima alcançada durante um teste de esforço físico'),
        html.P('- Indicação de se houve angina (dor no peito) induzida por exercício'),
        html.P('- Medida da depressão do segmento ST induzida pelo exercício em relação ao repouso'),
        html.P('- Inclinação do segmento ST no pico do exercício'),
        html.P('- Número de vasos sanguíneos principais coloridos durante o procedimento de fluoroscopia'),
        html.P('- Resultado do exame de cintilografia com tálio'),
        html.Br(),
        html.Br(),
    ], className = 'desloca-div'),

    div_rodape
])
