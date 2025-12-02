from dash import Dash, html, Input, Output, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_leaflet as dl
import base64

# import controller
from animal_shelter import AnimalShelter

# connect to database
db = AnimalShelter()

# import dataset as dataframe using pandas
df = pd.DataFrame.from_records(db.read({}))

# drop mongoDB objectId from each doc
df.drop(columns=['_id'], inplace=True)

# initialize dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.Center(html.B(html.H1('CS-340 Module 6 Dashboard'))),
    html.Hr(),
    dbc.Container([
        dbc.Label('Shelter Data'),
        dash_table.DataTable(data=df.to_dict('records'),columns=[{'name' : i, 'id' : i} for i in df.columns],
                         selectable=True, deletable=False, page_action='native', page_size=15, page_current=0),


    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)

