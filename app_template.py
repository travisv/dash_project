import pandas as pd
from dash import Dash,dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},],)

app.title = 'My App'

df = pd.read_feather('/home/travis/Desktop/dash_project/data/data.feather')
indicators = df.columns[14:]

app.layout = html.Div([
                        html.H3('Industry Page'),
                        dcc.Dropdown(df['Ticker'].unique(), id='ticker_dropdown', placeholder='Select a ticker'),
                        dcc.Dropdown(indicators, id='indicator_dropdown', value='Revenues'),
                        dcc.Graph(id='company_graph'),
                       # dcc.RangeSlider(dfe.Year.min(), 2022, step=1, value=[2000, 2020],
                       #                 marks={i: str(i) for i in range(df.Year.min(), 2023)},
                       #                 tooltip={"placement": "bottom", "always_visible": True})
])


@app.callback(
    Output('company_graph', 'figure'),
    Input('ticker_dropdown', 'value'),
    Input('indicator_dropdown', 'value'))
def company_revenue_bar_graph(ticker, indicator):
    mask = df['Ticker']==ticker
    tmp = df[mask].groupby('Year').sum()
    fig = go.Figure(data=[go.Bar(name='Graph', x=tmp.index, y=tmp[indicator])])
    #fig = px.bar(tmp, x='Year', y=tmp['Revenues'])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)


