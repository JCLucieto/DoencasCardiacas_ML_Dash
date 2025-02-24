# --------------------------------------------------------------
#   Criação de Modelo de Machine Learning Utilizando XGBoost
#---------------------------------------------------------------

# O modelo XGBoost (eXtreme Gradient Boosting) é uma implementação altamente eficiente de Gradient Boosting Machines (GBM), um algoritmo de aprendizado supervisionado.
# XGBoost é amplamente utilizado em competições de aprendizado de máquina e tem ganhado popularidade devido ao seu desempenho superior e flexibilidade.
# 
# Principais características do XGBoost:
# 
# Gradient Boosting: O XGBoost é baseado no método de boosting, que tenta melhorar o desempenho de um modelo fraco (geralmente uma árvore de decisão) iterativamente.
# Cada nova árvore tenta corrigir os erros da anterior, ajustando os pesos das amostras erradas.
# 
# Regularização: O XGBoost adiciona termos de regularização (L1 e L2) no modelo, ajudando a evitar o overfitting, o que não está presente na maioria dos algoritmos de 
# boosting tradicionais. Isso é feito através de parâmetros como lambda (para L2) e alpha (para L1).

# Paralelização: O XGBoost é altamente otimizado para execução rápida. Ele pode realizar paralelização em múltiplos núcleos de CPU, o que torna o treinamento de modelos
# muito mais rápido do que abordagens tradicionais.

# Handling Missing Values: O XGBoost pode lidar com valores ausentes de forma automática, sem a necessidade de imputação de dados, o que é muito útil em conjuntos de 
# dados incompletos.

# Categorização de Features: Embora as árvores de decisão tradicionalmente lidem bem com variáveis categóricas, o XGBoost oferece suporte eficiente para trabalhar com 
# dados categóricos sem a necessidade de uma codificação manual de variáveis.

# Custom Objective Functions: Você pode usar funções objetivo personalizadas, o que significa que o XGBoost pode ser adaptado para uma ampla variedade de problemas, 
# além de classificação e regressão.

# Early Stopping: Para evitar overfitting, o XGBoost tem uma funcionalidade de early stopping, onde o treinamento é interrompido se não houver melhoria na validação 
# após um número especificado de iterações.


# Imports

import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Carregar dados do arquivo dados_para_modelo.csv
# Esse arquivo já foi tratado no notebook (doencas_cardiacas.ipynb)

df_dados = pd.read_csv('../dados/dados_para_modelo.csv')

# Separa as colunas

y = df_dados['doenca']
X = df_dados.drop(columns='doenca')

# Criação de uma semente para reprodutividade

semente = 431

# Divide os dados em treino e teste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = semente, stratify=y)

# Cria DMatrix, estrutura de dados usada pelo XGBoost

dmatrix_treino = xgb.DMatrix(X_train, label = y_train)
dmatrix_teste  = xgb.DMatrix(X_test,  label = y_test)

# Define parâmetros para o modelo

params = {
    'objective': 'binary:logistic',   # Problema Binario (0 ou 1)
    'max_depth': 3,                   # Profundidade máxima das árvores
    'eta': 0.1,                       # Taxa de aprendizado
    'verbosity': 0                    # Exibe as informações de log (0=Nenhuma, 1=Basicas, 2=Detalhadas, 3=Todas)
}

# Treina o modelo

num_round = 100  # Número de iterações
modelo_xgb = xgb.train(params, dmatrix_treino, num_round)

# Fazer previsões
previsoes = modelo_xgb.predict(dmatrix_teste)

# Resultado (valores continuos)
#print (f'Previsões em Valores Continuos : \n = {previsoes}')

# Grava resultados
with open('resultados_modelo.txt', 'a') as arquivo:
    arquivo.write(f'\nPrevisoes em Valores Continuos : \n = {previsoes}\n')

# Converte previsoes em 0 ou 1 para poder usar metricas
# o algoritimo xgboost devolve valores continuos entre 0 e 1

previsoes = (previsoes > 0.5).astype(int)

# Resultados 0 ou 1
#print (f'Previsões em 0 ou 1 :\n {previsoes}')
# Grava resultados
with open('resultados_modelo.txt', 'a') as arquivo:
    arquivo.write(f'\nPrevisoes em 0 ou 1 : \n = {previsoes}\n')

# Acurácia

acuracia = accuracy_score(y_test, previsoes)
#print(f'A acurácia do modelo é {acuracia:.2%}')

# Criar um arquivo de texto e gravar a acurácia
with open('resultados_modelo.txt', 'a') as arquivo:
    arquivo.write(f'\nA Acuracia do Modelo : {acuracia:.2%}\n')

# Salva o Modelo

joblib.dump(modelo_xgb, 'modelo_xgboost.pkl')