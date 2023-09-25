# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Br(),
                                dcc.Dropdown(id='site-dropdown',
                                                options=[
                                                    {'label': 'All Sites', 'value': 'ALL'},
                                                    {'label': 'site1', 'value': 'site1'},
                                                ],
                                                value='ALL',
                                                placeholder="Select a Launch Site here",
                                                searchable=True
                                                ),
                                html.Br(),
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                ])
                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                # Function decorator to specify function input and output
                                @app.callback(Output(component_id='success-pie-chart', component_property='figure'),
                                              Input(component_id='site-dropdown', component_property='value'))
                                def get_pie_chart(entered_site):
                                    filtered_df = spacex_df
                                    if entered_site == 'ALL':
                                        fig = px.pie(filtered_df, names='class', title='Total Success Launches')
                                    else:
                                        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
                                        fig = px.pie(filtered_df, names='class', 
                                        title='Success vs. Failed for selected Launch Site')
                                    return fig,

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0', 100: '100'},
                                                value=[min_payload, max_payload],
                                                )
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                html.Br(),
                                @app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
                                              [Input(component_id='site-dropdown', component_property='value'),
                                               Input(component_id='payload-slider', component_property='value')])                                
                                def update_scatter_chart(selected_site, selected_payload):
                                    if selected_site == 'ALL':
                                        # For all sites
                                        fig = px.scatter(spacex_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                                                     title='Payload vs. Success (All Sites)')
                                    else:
                                        # For a specific launch site
                                        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
                                        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                                        title=f'Payload vs. Success for {selected_site} Launch Site')

                                    return fig,

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()