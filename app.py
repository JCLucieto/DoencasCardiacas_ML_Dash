#-------------------------------------------------------------------------
#  APLICAÇÃO DASH - (Criação de Dashboard - Doenças Cardíacas)
#  app.py - Estrutura para o app poder ser conhecido por todas as páginas
#-------------------------------------------------------------------------

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Cria a aplicação - Instancia de Dash

app = Dash(__name__,
           external_stylesheets = ['/assets/styles.css', dbc.themes.FLATLY],
           suppress_callback_exceptions = True)
