#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Here's a quick example

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


#Create a title for my Dashboard
app = dash.Dash(_name_)
server=app.server
app.layout = html.Div(children=[
    html.H1(style={'textAlign': 'center'}, children='Cloud Computing - Final Project'),
    html.Div(style={'textAlign': 'center'},children='''Author: Marc Cervera Castro (MIBA SECTION A)'''),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H3(style={'textAlign': 'center'}, children='Graph 1'),
    html.Div(children='''Choose the X variable: '''),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    html.Div(children='''Choose the Y variable:'''),
    
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'),
    html.Br(),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )}),
        dcc.Slider(
        min=1,
        max=8,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 9)},
        value=5),
        html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
    html.H3(style={'textAlign': 'center'}, children='Graph 2'),
    html.Div(children='''Choose the Countries you wish to see: '''),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    html.Div(children='''Choose the variable you wish to be graphed: '''),
    
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'),
    
    dcc.Graph(
        id='life-exp-vs-gdp_2',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )})
])

#Run the dashboard
if __name__ == '__main__':
    app.run_server(debug=False)

