import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Label('Dropdown',),
    dcc.Dropdown(
        id='dp1',
        options=[{'label':'Rio Grande do Sul', 'value':'RS'},
                {'label':'São Paulo', 'value':'SP'},
                {'label':'Paraná', 'value':'PR'},
],
        value='RS',style={'margin-bottom': '25px'}
),

html.Label('Chechlist'),
dcc.Checklist(
        id='cl-2',
        options=[{'label':'Rio Grande do Sul', 'value':'RS'},
                {'label':'São Paulo', 'value':'SP'},
                {'label':'Paraná', 'value':'PR'},
],
        value=['RS'],style={'margin-bottom': '25px'}
),

    html.Label('Text Input'),
    dcc.Input(value='SP', type='text'),


    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=10,
        marks={1: 'Label{}'.format(i if i==1 else str(i) for i in range(1,6))},
        value = 5
    )




])

if __name__ == '__main__':
    app.run_server(debug=True)