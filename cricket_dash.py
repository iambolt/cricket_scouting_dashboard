import pandas as pd
import plotly.express as px  
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

data_smat_2019 = pd.read_csv('./data/data_smat_2019.csv')
data_smat_2020 = pd.read_csv('./data/data_smat_2020.csv')
data_smat_2021 = pd.read_csv('./data/data_smat_2021.csv')

app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H1("Players Performance Dashboard (India Domestic)"),
                html.H5("Nishant Singh Siddhu"),
            ], width={'size': 9, 'offset':2}),]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Key Parameters"),
                    html.P("Select the Series"),
                    
                    dcc.Dropdown(
                            id='dd_trophy',
                            options=[
                                {'label': 'SYED MUSHTAQ ALI TROPHY', 'value': 'smat'},
                                {'label': 'VIJAY HAZARE TROPHY', 'value': 'vht'}
                                ],),

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
                    html.H5("Select Batter type"),
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
                ),
                dbc.Spinner(
                    dcc.Graph(id='display_scat', style={'height': '80vh'}),
                    color="primary"
                ) 
            ], width=True)



        ]),

        # dbc.Row([
        #     dbc.Col([
        #         # html.Div(id='display')
        #         dbc.Spinner(
        #             dcc.Graph(id='display_scat', style={'height': '80vh'}),
        #             color="primary"
        #         )
        #     ], width=True),

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

@app.callback(
    [Output('display', 'figure'),
    Output('display_scat', 'figure')],
    [
        Input('dd_trophy', 'value'),
        Input('year', 'value'),
        Input('display_op', 'n_clicks_timestamp'),
        Input('display_mo', 'n_clicks_timestamp'),
        Input('display_lmo', 'n_clicks_timestamp'),
        Input('display_wkb', 'n_clicks_timestamp'),
    ],
)

def display_plot(trophy_val,year_val, opener_val, middle_val, lower_val, wk_val):
    
    print(trophy_val,year_val, opener_val, middle_val, lower_val, wk_val)

    try:
        button_pressed = np.argmax(np.array([
            float(opener_val),
            float(middle_val),
            float(lower_val),
            float(wk_val),
        ]))
        assert button_pressed is not None
    except:
        button_pressed = 0

    if trophy_val == 'smat':
        if year_val == 2021:
            if button_pressed == 0:
                fig = px.scatter_3d(data_smat_2021.iloc[:10], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[:10], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 1:
                fig = px.scatter_3d(data_smat_2021.iloc[10:21], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[10:21], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 2:
                fig = px.scatter_3d(data_smat_2021.iloc[21:29], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[21:29], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 3:
                fig = px.scatter_3d(data_smat_2021.iloc[29:], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[29:], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
        elif year_val == 2020:
            if button_pressed == 0:
                fig = px.scatter_3d(data_smat_2020.iloc[:10], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[:10], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 1:
                fig = px.scatter_3d(data_smat_2020.iloc[10:20], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[10:20], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 2:
                fig = px.scatter_3d(data_smat_2020.iloc[20:27], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[20:27], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 3:
                fig = px.scatter_3d(data_smat_2020.iloc[27:], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[27:], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
        elif year_val == 2019:
            if button_pressed == 0:
                fig = px.scatter_3d(data_smat_2019.iloc[:10], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[:10], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 1:
                fig = px.scatter_3d(data_smat_2019.iloc[10:20], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[10:20], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 2:
                fig = px.scatter_3d(data_smat_2019.iloc[20:28], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[20:28], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 3:
                fig = px.scatter_3d(data_smat_2019.iloc[28:], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[28:0], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])

    if trophy_val == 'vht':
        if year_val == 2021:
            if button_pressed == 0:
                fig = px.scatter_3d(data_smat_2021.iloc[:10], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[:10], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 1:
                fig = px.scatter_3d(data_smat_2021.iloc[10:21], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[10:21], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 2:
                fig = px.scatter_3d(data_smat_2021.iloc[21:29], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[21:29], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 3:
                fig = px.scatter_3d(data_smat_2021.iloc[29:], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2021.iloc[29:0], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
        elif year_val == 2020:
            if button_pressed == 0:
                fig = px.scatter_3d(data_smat_2020.iloc[:10], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[:10], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 1:
                fig = px.scatter_3d(data_smat_2020.iloc[10:20], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[10:20], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 2:
                fig = px.scatter_3d(data_smat_2020.iloc[20:27], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[20:27], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 3:
                fig = px.scatter_3d(data_smat_2020.iloc[27:], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2020.iloc[27:0], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
        elif year_val == 2019:
            if button_pressed == 0:
                fig = px.scatter_3d(data_smat_2019.iloc[:10], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[:10], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])

            elif button_pressed == 1:
                fig = px.scatter_3d(data_smat_2019.iloc[10:20], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[10:20], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 2:
                fig = px.scatter_3d(data_smat_2019.iloc[20:28], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[20:28], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
            elif button_pressed == 3:
                fig = px.scatter_3d(data_smat_2019.iloc[28:], x='Runs', y='Avg', z='SR', color ='Player')
                fig2= px.scatter(data_smat_2019.iloc[28:], x="BRPI", y="MRA", color="Player",size='SR', hover_data=['Runs','Inns'])
    fig.update_layout(scene=dict(
                                     xaxis=dict(backgroundcolor="rgb(200, 200, 230)",gridcolor="white", 
                                                showbackground=True,zerolinecolor="white",),
                                     yaxis=dict(backgroundcolor="rgb(230, 200,230)",gridcolor="white", 
                                                showbackground=True,zerolinecolor="white",),
                                     zaxis=dict(backgroundcolor="rgb(230, 230,200)",gridcolor="white", 
                                                showbackground=True,zerolinecolor="white",),
                                     bgcolor='cadetblue'),
                             plot_bgcolor='rgb(12,163,135)',
                         )

    print(button_pressed)
    
    return fig,fig2



if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)
