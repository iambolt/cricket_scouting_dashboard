import pandas as pd
import plotly.express as px  

import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


app.layout = html.Div([

    html.H1("Players Performances Dashboard (India Domestic)", style={'text-align': 'center'}),

    html.P("Select a Series", style={'text-align': 'left'}),
    dcc.Dropdown(
    options=[
        {'label': 'SYED MUSHTAQ ALI TROPHY', 'value': 'SMAT'},
        {'label': 'VIJAY HAZARE TROPHY', 'value': 'VHT'}],
        multi=False,
        style={'width': "40%"},
        placeholder="Select a Series",),

    html.Div([ dcc.Slider(
    min=2019,
    max=2021,
    value=2021,
    marks={
        2019: {'label': '2019'},
        2020: {'label': '2020'},
        2021: {'label': '2021'},
    },
    included=False),
    ],
    style={'width': "40%",'padding-left':'25%', 'padding-right':'25%'}),
  

    


    html.Div(id='output_container', children=[]),
    html.Br(),


    dcc.Graph(id='my_bee_map', figure={})

])



if __name__ == '__main__':
    app.run_server(debug=False)
