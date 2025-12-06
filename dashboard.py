

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
app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

# encode logo to base64 string
binary_img = open('Grazioso Salvare Logo.png', 'rb').read()
encoded_img = base64.b64encode(binary_img)

app.layout = dbc.Container([
    html.Center(html.B(html.H1('CS-340 Module 6 Dashboard'))),
    html.Br(),
    html.Br(),
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    # Anchor component with requested logo and link
                    html.A([
                        html.Img(
                            src='data:image/png;base64,{}'.format(encoded_img.decode()),
                            style={
                                'height': '300px',
                                'width': 'auto',
                                'objectFit': 'contain'
                            }
                        )
                    ], href='https://www.snhu.edu', target='_blank')
                ], xs=12, md=4, className='d-flex align-items-center justify-content-center'),
                dbc.Col([
                    html.H2('Welcome to the Grazioso Salvare Dashboard', className='card-title mb-3 mt-2'),
                    html.P([
                        "This dashboard helps identify rescue dog candidates from Austin-area animal shelters. "
                        "Use the filters below to search for dogs matching specific rescue profiles: ",
                        html.Br(),
                        html.Strong("Water Rescue"), ", ",
                        html.Strong("Mountain/Wilderness Rescue"), ", or ",
                        html.Strong("Disaster/Individual Tracking"), ". ",
                        html.Br(),
                        "Each rescue type has preferred breed, age, and sex criteria optimized for training success.",
                    ], className='card-text mb-3'),
                    html.P("This dashboard was built by Sarah Dowd 💾",
                       className='text-muted small')
                ], xs=12, md=8, className='mb-4'),
            ], className='mb-4 d-flex align-items-center'),
        ])
    ], style={ 'backgroundColor' : '#faf8f5' }, className='shadow-sm mb-4 m-5'),
    # container for DataTable
    dbc.Container([
        html.H3('Shelter Data'),
        dbc.Card([
           dbc.CardBody([
               html.H5('Filter by Rescue Type', className='card-title'),
                # dropdown menu with rescue options to filter data displayed in table, placeholder text instructs user
                dcc.Dropdown(['Water Rescue', 'Mountain Rescue', 'Disaster Rescue', 'Reset'],
                            placeholder='Select Rescue Type', id='dropdown-filter',
                             style=
                                {
                                    'color': '#2c3e50',
                                }),
           ], style={'color': 'white',
                    'backgroundColor': '#2c3e50',
                     'borderRadius': '8px'},
                className='p-3'),
        ]),
        # data table built from data from database--selectable rows, native pagination, 10 rows per page
        # cells left-aligned with max width, table scrolls horizontally, sorting enabled
        dash_table.DataTable(data=df.to_dict('records'),
                            columns=[
                                {
                                    'name' : i.replace('_', ' ').title(), # transform from snake case to title case
                                    'id' : i,
                                    'deletable' : False,
                                    'selectable' : True
                                } for i in df.columns],
                            row_selectable='single',
                            page_action='native',
                            sort_action='native',
                            page_size=10,
                            page_current=0,
                            id='shelter-table',
                            style_cell=
                                {
                                    'textAlign' : 'left',
                                    'height': 'auto',
                                    'minWidth': '90px',
                                    'width': '180px',
                                    'maxWidth': '180px',
                                    'textOverflow' : 'ellipsis',
                                },
                            style_table=
                                {
                                    'overflowX': 'auto',
                                    'borderRadius': '8px'
                                },
                            style_data=
                                {
                                    'backgroundColor': '#faf8f5',
                                    'fontFamily': '"Ubuntu", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                                },
                            style_header=
                                {
                                    'color': 'white',
                                    'backgroundColor': '#2c3e50',
                                    'fontFamily': '"Ubuntu", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                                },
                                css=[{
                                        'selector': 'input[type="radio"]:checked',
                                        'rule': 'accent-color: #c9341b;'
                                    }],
                            selected_rows=[0]),
    ]),
    html.Br(),
    # container for graph and map -- wrapped in a row for optimized layout
    dbc.Container([
        dbc.Row([
            dbc.Col(
                [dcc.Graph(id='pie-chart')], xs=12, md=6
            ),
            dbc.Col(
                [html.H5('Selected Animal Location', className='mb-2'),
                 html.Div(id='map-div')
                 ], xs=12, md=6
            )
        ])
    ], fluid=True),
    html.Br(),
    html.Br(),

], fluid='true', className='p-4', style={'backgroundColor': '#F2E6E3'})

# callback to update datatable by filtering data based on dropdown selection
@app.callback(
    Output('shelter-table', 'data'),
    Output('shelter-table', 'selected_rows'),
    Input('dropdown-filter', 'value')
)
def update_table(dropdown_filter):
    # create query for each dropdown filter based on given Grazioso Salvare criteria
    if dropdown_filter == 'Water Rescue':
        query = {
            'breed': {'$in': ['Labrador Retriever Mix', 'Chesapeake Bay Retriever', 'Newfoundland']},
            'sex_upon_outcome': 'Intact Female',
            'age_upon_outcome_in_weeks': {'$gte': 26, '$lte': 156}
        }
    elif dropdown_filter == 'Mountain Rescue':
        query = {
            'breed': {'$in': ['German Shepherd', 'Alaskan Malamute',
                              'Old English Sheepdog', 'Siberian Husky', 'Rottweiler']},
            'sex_upon_outcome': 'Intact Male',
            'age_upon_outcome_in_weeks': {'$gte': 26, '$lte': 156}
        }
    elif dropdown_filter == 'Disaster Rescue':
        query = {
            'breed': {'$in': ['Doberman Pinscher', 'German Shepherd',
                              'Golden Retriever', 'Bloodhound', 'Rottweiler']},
            'sex_upon_outcome': 'Intact Male',
            'age_upon_outcome_in_weeks': {'$gte': 20, '$lte': 300}
        }
    # reset option passes in empty query as in first df construct
    else:
        query = {}
    # pass dropdown_filter query into db.read to create new filtered dataframe & drop objectid
    filtered_df = pd.DataFrame.from_records(db.read(query))
    filtered_df.drop(columns=['_id'], inplace=True)
    # return filtered dataframe to data property of DataTable
    return filtered_df.to_dict('records'), [0]
# TODO callback to highlight selected row in data table
# callback to display breed percentages in pie chart
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('shelter-table', 'derived_virtual_data')]
)
def update_pie_chart(viewData):
    if viewData is None:
        return {}

    # pie dataframe from shelter-table data
    pie_df = pd.DataFrame.from_records(viewData)
    if pie_df.empty:
        return {}
    # filter to display top 8 breeds -- otherwise full df pie chart looks like nonsense
    top_breeds = pie_df['breed'].value_counts().head(8).reset_index()
    top_breeds.columns = ['breed', 'count']
    # construct pie chart with plotly express
    fig = px.pie(
        top_breeds,
        names='breed',
        values='count',
        title='Breed Distribution',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    # customize with update_traces method
    fig.update_traces(
        hovertemplate='<b>%{label}</b><br>Dogs Available: %{value}<br>Percentage: %{percent}<extra></extra>',
        textposition='inside',
        textinfo='percent',
        marker=dict(line=dict(color='white', width=2))
    )
    # match style of page with update_layout method
    fig.update_layout(
        paper_bgcolor='#F2E6E3',
        font={'family' : 'ubuntu'},
        title_font={'size' : 22}
    )
    return fig

@app.callback(
    Output('map-div', "children"),
    [Input('shelter-table', "derived_virtual_data"),
     Input('shelter-table', "derived_virtual_selected_rows")])
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
        dl.Map(style={'width': '100%', 'height': '500px'},
               center=[dff.iloc[row, 13], dff.iloc[row, 14]], # changed map center from Austin to selected row loc
               zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            # Marker with tool tip and popup
            # Column 13 and 14 define the grid-coordinates for the map
            dl.Marker(position=[dff.iloc[row, 13], dff.iloc[row, 14]], children=[
                # Column 4 defines the breed for the animal
                dl.Tooltip(dff.iloc[row, 4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    # Column 9 defines the name of the animal
                    html.P(dff.iloc[row, 9])
                ])
            ])
        ])
    ]

if __name__ == '__main__':
    app.run(debug=True)

