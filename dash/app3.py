import dash
from dash import html, dcc
from dash.dependencies import Input, Output,State

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H3('Altere o valor abaixo usando callback'),
    html.Div(['Entrada:', dcc.Input(id='my-input',value='valor inicial', type='text')]),


    html.Br(),
    html.Div(id='my-output'),
])


@app.callback(
    Output(component_id='my-output',component_property='children'),
    [Input(component_id='my-input',component_property='value')]
)

def update_output_div(value):
    return 'Saida:{}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)