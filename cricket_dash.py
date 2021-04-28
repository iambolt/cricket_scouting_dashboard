import pandas as pd
import plotly.express as px  

import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H2("Players Performance Dashboard (India Domestic)"),
                html.H5("Nishant Singh Siddhu"),
            ], width={'size': 9, 'offset':2}),]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Key Parameters"),
                    html.P("Select the Series"),
                    
                    dbc.DropdownMenu(
                                id='n_trophy',
                                label="Select",
                                children=[
                                    dbc.DropdownMenuItem("SYED MUSHTAQ ALI TROPHY",id="dropdown_smat"),
                                    dbc.DropdownMenuItem("VIJAY HAZARE TROPHY",id="dropdown_vjt")],
                                    style={"display": "flex", "flexWrap": "wrap"}),
                    html.Hr(),
                    html.P("Select the year"), 
                    dcc.Slider(
                    id='year',
                    min=2019,
                    max=2021,
                    value=2021,
                        marks={
                            2019: '2019',
                            2020: '2020',
                            2021: '2021',
                            },included=False),
                ]),
                html.Hr(),
                html.Div([
                    html.H5("Select Batsmen type"),
                    dbc.Button("Openers", id="display_op", color="dark", style={"margin": "5px"},
                               n_clicks_timestamp='0'),
                    dbc.Button("Middle Order", id="display_mo", color="dark", style={"margin": "5px"},
                               n_clicks_timestamp='0'),
                    dbc.Button("Lower Middle Order", id="display_lmo", color="dark",
                               style={"margin": "5px"}, n_clicks_timestamp='0'),
                    dbc.Button("Wicket keepers", id="display_wkb", color="dark",
                               style={"margin": "5px"}, n_clicks_timestamp='0'),
                ]),
                html.Hr(),

            ], width=3),

            dbc.Col([
                # html.Div(id='display')
                dbc.Spinner(
                    dcc.Graph(id='display', style={'height': '80vh'}),
                    color="primary"
                )
            ], width=True)

        ]),
        html.Hr(),
        html.P([
            html.A("Source code", href="https://github.com/iambolt/cricket_scouting_dashboard"),
            ". Build beautiful UIs for your scientific computing apps with ",
            html.A("Plot.ly ", href="https://plotly.com/"),
            "and ",
            html.A("Dash", href="https://plotly.com/dash/"),
            "!",
        ]),
    ],
    fluid=True
)




if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)
