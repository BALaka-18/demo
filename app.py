import numpy as np
import pandas as pd
import dash
import plotly.graph_objs as go
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Configuring
# external CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous',
    }
]

cov = pd.read_csv('covid_19_data.csv')
recov = pd.read_csv('time_series_covid_19_recovered.csv')
death = pd.read_csv('time_series_covid_19_deaths.csv')
conf = pd.read_csv('time_series_covid_19_confirmed.csv')
cont_rec = pd.DataFrame(
    recov.groupby('Country/Region')['4/3/20']
    .sum()
    .sort_values(ascending=False)
).reset_index()
cont_dec = pd.DataFrame(
    death.groupby('Country/Region')['4/3/20']
    .sum()
    .sort_values(ascending=False)
).reset_index()
cont_conf = pd.DataFrame(
    conf.groupby('Country/Region')['4/3/20'].sum().sort_values(ascending=False)
).reset_index()
"""rec = sum(cont_rec['4/3/20'].values)
deaths = sum(cont_dec['4/3/20'].values)
confirmed = sum(cont_conf['4/3/20'].values)"""

indx_lst1 = list(
    cov.groupby('Country/Region')['Confirmed']
    .agg(sum)
    .sort_values(ascending=False)
    .head(5)
    .index
)
new1 = cov[cov['Country/Region'].isin(indx_lst1)]
indx_lst2 = list(
    cov.groupby('Country/Region')['Deaths']
    .agg(sum)
    .sort_values(ascending=False)
    .head(5)
    .index
)
new2 = cov[cov['Country/Region'].isin(indx_lst2)]

# Updated values
confirmed = 1202236
rec = 246457
deaths = 64753

cov['Month'] = 0
for i in range(cov.shape[0]):
    cov.iloc[i, 8] = int(cov.iloc[i, 1][0:2])
month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4}

countries = list(cov['Country/Region'].unique())
options, options2 = [], []
for c in countries:
    label = c
    value = c
    options.append({'label': label, 'value': value})

options2 = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Confirmed', 'value': 'Confirmed'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deaths', 'value': 'Deaths'},
]

options3 = [
    {'label': 'January', 'value': 'January'},
    {'label': 'February', 'value': 'February'},
    {'label': 'March', 'value': 'March'},
    {'label': 'April', 'value': 'April'},
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div(
    [
        html.H1(
            [
                html.A(
                    'CORONA VIRUS PANDEMIC',
                    href='https://www.worldometers.info/coronavirus/',
                )
            ],
            style={
                'color': '#FFF',
                'text-align': 'center',
                'font-family': 'Lucida Console',
                'font-weight': 'bold',
            },
        ),
        html.Br(),
        html.H5(
            'Stop this pandemic from spreading. Stay Home. Wash Hands. Stay Safe.',
            style={
                'color': '#FFF',
                'text-align': 'center',
                'font-family': 'Lucida Console',
                'font-weight': 'bold',
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3(
                                            'Total Cases',
                                            style={'color': '#fff'},
                                        ),
                                        html.H4(
                                            confirmed, style={'color': '#fff'}
                                        ),
                                    ],
                                    className='card-body',
                                )
                            ],
                            className='card bg-danger',
                            style={'margin-top': '50px'},
                        )
                    ],
                    className='col-md-4',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3(
                                            'Recovered',
                                            style={'color': '#fff'},
                                        ),
                                        html.H4(rec, style={'color': '#fff'}),
                                    ],
                                    className='card-body',
                                )
                            ],
                            className='card bg-warning',
                            style={'margin-top': '50px'},
                        )
                    ],
                    className='col-md-4',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3(
                                            'Deaths', style={'color': '#fff'}
                                        ),
                                        html.H4(
                                            deaths, style={'color': '#fff'}
                                        ),
                                    ],
                                    className='card-body',
                                )
                            ],
                            className='card bg-success',
                            style={'margin-top': '50px'},
                        )
                    ],
                    className='col-md-4',
                ),
            ],
            className='row',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id='pie1',
                                            figure=go.Figure(
                                                data=[
                                                    go.Pie(
                                                        values=[
                                                            1202236,
                                                            246457,
                                                            64753,
                                                        ],
                                                        labels=[
                                                            'Confirmed',
                                                            'Recovered',
                                                            'Deceased',
                                                        ],
                                                    )
                                                ],
                                                layout=go.Layout(
                                                    title='COVID-19 EFFECT AROUND THE WORLD'
                                                ),
                                            ),
                                        )
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-6',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id='pie2',
                                            figure=go.Figure(
                                                data=[
                                                    go.Pie(
                                                        values=[3374, 267, 77],
                                                        labels=[
                                                            'Confirmed',
                                                            'Recovered',
                                                            'Deceased',
                                                        ],
                                                    )
                                                ],
                                                layout=go.Layout(
                                                    title='COVID-19 EFFECT IN INDIA'
                                                ),
                                            ),
                                        )
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-6',
                ),
            ],
            className='row',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id='picker1',
                                            options=options,
                                            value='US',
                                        ),
                                        dcc.Graph(id='bar'),
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-12',
                )
            ],
            className='row',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id='picker2',
                                            options=options2,
                                            value='All',
                                        ),
                                        dcc.Graph(id='bar2'),
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-12',
                )
            ],
            className='row',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id='heat1',
                                            figure=go.Figure(
                                                data=[
                                                    go.Heatmap(
                                                        x=new1[
                                                            'Country/Region'
                                                        ],
                                                        y=new1[
                                                            'ObservationDate'
                                                        ],
                                                        z=new1['Confirmed'],
                                                    )
                                                ],
                                                layout=go.Layout(
                                                    title='TOP 5 COUNTRIES TIME HEATMAP OF CONFIRMED CASES'
                                                ),
                                            ),
                                        )
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-6',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id='heat2',
                                            figure=go.Figure(
                                                data=[
                                                    go.Heatmap(
                                                        x=new2[
                                                            'Country/Region'
                                                        ],
                                                        y=new2[
                                                            'ObservationDate'
                                                        ],
                                                        z=new2['Deaths'],
                                                    )
                                                ],
                                                layout=go.Layout(
                                                    title='TOP 5 COUNTRIES TIME HEATMAP OF DEACEASED CASES'
                                                ),
                                            ),
                                        )
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-6',
                ),
            ],
            className='row',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id='picker3',
                                            options=options3,
                                            value='April',
                                        ),
                                        dcc.Dropdown(
                                            id='picker4',
                                            options=options2,
                                            value='All',
                                        ),
                                        dcc.Graph(id='bar3'),
                                    ],
                                    className='card=body',
                                )
                            ],
                            className='card',
                            style={'margin-top': '30px'},
                        )
                    ],
                    className='col-md-12',
                )
            ],
            className='row',
        ),
        html.Br(),
        html.H6(
            'Dashboard by Balaka Biswas',
            style={
                'color': '#FFBAC4',
                'text-align': 'right',
                'font-family': 'Lucida Console',
                'font-weight': 'bold',
            },
        ),
        html.Br(),
    ],
    className='container',
    style={'margin-top': '50px'},
)


@app.callback(
    Output('bar', 'figure'), [Input('picker1', 'value')]
)  # Output(id_to_give_output_to, parameter_to_return)   Input(id,parameter)
def update_graph(type):
    choice = cov[cov['Country/Region'] == type]
    count = pd.DataFrame(
        choice.groupby('Province/State')['Confirmed']
        .sum()
        .sort_values(ascending=False)
    ).reset_index()
    return {
        'data': [go.Bar(x=count['Province/State'], y=count['Confirmed'])],
        'layout': go.Layout(
            title='PROVINCE/STATE WISE COUNT FOR COUNTRY OF YOUR CHOICE'
        ),
    }


@app.callback(
    Output('bar2', 'figure'), [Input('picker2', 'value')]
)  # Output(id_to_give_output_to, parameter_to_return)   Input(id,parameter)
def update_graph(type):
    if type == 'All':
        t1 = pd.DataFrame(
            cov.groupby('Country/Region')['Confirmed']
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        t2 = pd.DataFrame(
            cov.groupby('Country/Region')['Deaths']
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        t3 = pd.DataFrame(
            cov.groupby('Country/Region')['Recovered']
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        trace1 = go.Bar(
            x=t1['Country/Region'],
            y=t1['Confirmed'],
            marker={'color': '#00a65a'},
            name='Confirmed',
        )
        trace2 = go.Bar(x=t2['Country/Region'], y=t2['Deaths'], name='Deaths')
        trace3 = go.Bar(
            x=t3['Country/Region'],
            y=t3['Recovered'],
            marker={'color': '#a6a65a'},
            name='Recovered',
        )
        return {
            'data': [trace1, trace2, trace3],
            'layout': go.Layout(
                title='TOTAL NUMBER OF CASES(CONFIRMED,DECEASED,RECOVERD) PER COUNTRY',
                barmode='stack',
            ),
        }
    else:
        data = pd.DataFrame(
            cov.groupby('Country/Region')[type]
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        return {
            'data': [go.Bar(x=data['Country/Region'], y=data[type])],
            'layout': go.Layout(
                title='TOTAL NUMBER OF CASES PER COUNTRY BASED ON CHOICE'
            ),
        }


@app.callback(
    Output('bar3', 'figure'),
    [Input('picker3', 'value'), Input('picker4', 'value')],
)  # Output(id_to_give_output_to, parameter_to_return)   Input(id,parameter)
def update_graph(type1, type2):
    month = cov[cov['Month'] == month_dict[type1]]
    if type2 == 'All':
        t1 = pd.DataFrame(
            month.groupby('Country/Region')['Confirmed']
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        t2 = pd.DataFrame(
            month.groupby('Country/Region')['Deaths']
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        t3 = pd.DataFrame(
            month.groupby('Country/Region')['Recovered']
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        trace1 = go.Bar(
            x=t1['Country/Region'],
            y=t1['Confirmed'],
            marker={'color': '#00a65a'},
            name='Confirmed',
        )
        trace2 = go.Bar(x=t2['Country/Region'], y=t2['Deaths'], name='Deaths')
        trace3 = go.Bar(
            x=t3['Country/Region'],
            y=t3['Recovered'],
            marker={'color': '#a6a65a'},
            name='Recovered',
        )
        return {
            'data': [trace1, trace2, trace3],
            'layout': go.Layout(
                title='TOTAL NUMBER OF CASES(CONFIRMED,DECEASED,RECOVERD) PER COUNTRY PER MONTH BASED ON CHOICE',
                barmode='stack',
            ),
        }
    else:
        data = pd.DataFrame(
            month.groupby('Country/Region')[type2]
            .agg(sum)
            .sort_values(ascending=False)
        ).reset_index()
        return {
            'data': [go.Bar(x=data['Country/Region'], y=data[type2])],
            'layout': go.Layout(
                title='TOTAL NUMBER OF CASES PER COUNTRY PER MONTH BASED ON CHOICE'
            ),
        }


"""@app.callback(Output('pie1','figure'))              # Output(id_to_give_output_to, parameter_to_return)   Input(id,parameter)
def update_graph():
    return {'data': [go.Figure(data = [go.Pie(values = [1202236,246457,64753],labels=['Confirmed','Recovered','Deceased'])])]}"""


if __name__ == '__main__':
    app.run_server(debug=True)
