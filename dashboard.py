from dash import Dash, html, Input, Output, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_leaflet as dl
import base64

import importlib
import animal_shelter

# Reload the module
importlib.reload(animal_shelter)
# import controller
from animal_shelter import AnimalShelter

# connect to database
db = AnimalShelter()

# import dataset as dataframe using pandas
df = pd.DataFrame.from_records(db.read({}))

# drop mongoDB objectId from each doc
df.drop(columns=['_id'], inplace=True)

# initialize dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])


app.layout = html.Div([
    html.Center(html.B(html.H1('CS-340 Module 6 Dashboard'))),
    html.Hr(),
    dbc.Container([
        dbc.Label('Shelter Data'),
        # dropdown menu with rescue options to filter data displayed in table, placeholder text instructs user
        dcc.Dropdown(['Water Rescue', 'Mountain Rescue', 'Disaster Rescue', 'Reset'],
                     placeholder='Select Rescue Type to Filter Data'),
        dash_table.DataTable(data=df.to_dict('records'),
                            columns=[{'name' : i, 'id' : i, 'deletable' : False, 'selectable' : True} for i in df.columns],
                            row_selectable='single', page_action='native', page_size=15, page_current=0, id='shelter-table')
    ]),
    html.Br,
    html.Div(id='map-div'),
    html.Br(),
    html.Br(),

])


@app.callback(
    Output('map-div', "children"),
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")])
def update_map(viewData, index):
    if viewData is None:
        return None
    elif index is None:
        return None

    dff = pd.DataFrame.from_dict(viewData)
    # Because we only allow single row selection, the list can be converted to a row index here
    if index is None:
        row = 0
    else:
        row = index[0]

    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[30.75, -97.48], zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            # Marker with tool tip and popup
            # Column 13 and 14 define the grid-coordinates for the map
            # Column 4 defines the breed for the animal
            # Column 9 defines the name of the animal
            dl.Marker(position=[dff.iloc[row, 13], dff.iloc[row, 14]], children=[
                dl.Tooltip(dff.iloc[row, 4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(dff.iloc[row, 9])
                ])
            ])
        ])
    ]

if __name__ == '__main__':
    app.run(debug=True)

