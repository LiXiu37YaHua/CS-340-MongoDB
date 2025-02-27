#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash import Dash, dcc, html
import dash_table
import pandas as pd
import plotly.express as px
import dash_leaflet as dl
from dash.dependencies import Input, Output

# Path to the uploaded CSV file in the assets folder
file_path = 'assets/aac_shelter_outcomes (2).csv'  # Adjust path if necessary

# Initialize the Dash app
app = Dash(__name__)

# Load the data from the CSV file
df = pd.read_csv(file_path)

# Clean the data by removing rows with missing or invalid latitude and longitude
df_clean = df.dropna(subset=['location_lat', 'location_long'])

# Remove rows with invalid latitudes and longitudes (lat: -90 to 90, lon: -180 to 180)
df_clean = df_clean[~((df_clean['location_lat'] < -90) | (df_clean['location_lat'] > 90) | 
                     (df_clean['location_long'] < -180) | (df_clean['location_long'] > 180))]

# Layout for the Dashboard
app.layout = html.Div([

    # Display the Grazioso Salvare logo
    html.Center(children=[ 
        html.H1("SNHU CS-340 Marissa Lanza"),
        # Correct image path for the assets folder
        html.Img(src='/assets/Grazioso Salvare Logo.png', style={'width': '200px', 'height': '200px'})
    ]),

    # Dropdown for Outcome Type Filter and Dog Breed Filter
    html.Div([  
        dcc.Dropdown(
            id='outcome-type-dropdown',
            options=[
                {'label': 'Transfer', 'value': 'Transfer'},
                {'label': 'Adoption', 'value': 'Adoption'},
                {'label': 'Return to Owner', 'value': 'Return to Owner'},
                {'label': 'Euthanasia', 'value': 'Euthanasia'},
                {'label': 'Disaster Rescue Dog', 'value': 'Disaster Rescue Dog'}  # Add this option for Disaster Rescue Dogs
            ],
            value='Adoption',  # Default value
            style={'width': '48%', 'padding': '3px'}
        ),
        dcc.Dropdown(
            id='breed-dropdown',
            options=[ 
                {'label': 'German Shepherd', 'value': 'German Shepherd'},
                {'label': 'Labrador', 'value': 'Labrador'},
                {'label': 'Beagle', 'value': 'Beagle'},
                {'label': 'Golden Retriever', 'value': 'Golden Retriever'}
            ],
            value='German Shepherd',  # Default value
            style={'width': '48%', 'padding': '3px'}
        )
    ], style={'display': 'flex', 'justify-content': 'space-between', 'margin': '20px'}),

    # Button to filter for Disaster Rescue Dogs
    html.Div([ 
        html.Button("Show Disaster Rescue Dogs", id="disaster-button", n_clicks=0),
    ], style={'padding': '20px', 'textAlign': 'center'}),

    # Interactive Data Table
    dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",  # Allow filtering
        sort_action="native",  # Allow sorting
        sort_mode="multi",  # Allow multi-column sorting
        column_selectable="single",  # Allow single column selection
        row_selectable="single",  # Allow single row selection
        row_deletable=False,  # Disable row deletion
        selected_columns=[],  # Initially no columns selected
        selected_rows=[],  # Initially no rows selected
        page_action="native",  # Enable pagination
        page_current=0,  # Set the start page to 0
        page_size=10,  # Set rows per page to 10
    ),

    # Pie Chart for Breed Distribution and Geolocation Map
    html.Div([ 
        dcc.Graph(id='pie-chart', style={'width': '50%', 'display': 'inline-block'}),
        html.Div(id='geo-map', style={'width': '50%', 'display': 'inline-block'}) 
    ], style={'margin': '20px'}), 
])

@app.callback(
    Output('data-table', 'data'),
    Output('pie-chart', 'figure'),
    Output('geo-map', 'children'),
    [Input('outcome-type-dropdown', 'value'),
     Input('breed-dropdown', 'value'),
     Input('disaster-button', 'n_clicks')]
)
def update_dashboard(outcome_type, breed, n_clicks):
    # Filter for Disaster Rescue Dogs when the button is clicked
    if n_clicks > 0:
        filtered_df = df_clean[df_clean['outcome_type'] == 'Disaster Rescue Dog']
    else:
        filtered_df = df_clean[(df_clean['outcome_type'] == outcome_type) & (df_clean['breed'] == breed)]
    
    # Check if filtered data is empty
    if filtered_df.empty:
        return [], go.Figure(), None

    # Update Data Table
    table_data = filtered_df.to_dict('records')

    # Create Pie Chart for All Breeds Distribution (Unfiltered)
    breed_counts = df_clean['breed'].value_counts().reset_index()  # Count occurrences of each breed
    breed_counts.columns = ['breed', 'count']  # Rename columns for pie chart

    # Create Pie Chart for all breeds with custom styling
    pie_fig = px.pie(breed_counts, 
                     names='breed', 
                     values='count', 
                     title="Breed Distribution of Animals",
                     color='breed',
                     color_discrete_sequence=px.colors.qualitative.Pastel)  # Choose a color scheme
    
    # Customize pie chart to match the style in the image
    pie_fig.update_traces(textinfo='percent+label', pull=[0.1, 0.1, 0.1, 0.1])  # Adds labels and separation for better visualization
    pie_fig.update_layout(
        plot_bgcolor='black',  # Set the background color to black
        paper_bgcolor='black',  # Set paper background color to black
        font_color='white',  # Change font color to white
        title_font_size=24,  # Increase title font size
        title_x=0.5,  # Center align the title
        margin=dict(t=0, b=0, l=0, r=0)  # Remove margins around the chart
    )

    # Geolocation Map with dash-leaflet
    geo_map = []
    if 'location_lat' in filtered_df.columns and 'location_long' in filtered_df.columns:
        for _, row in filtered_df.iterrows():
            geo_map.append(dl.Marker(position=[row['location_lat'], row['location_long']], 
                                     children=[dl.Popup(html.P(f"Dog Name: {row['name']}"))]))

        geo_map = dl.Map(style={'width': '100%', 'height': '500px'},
                         center=[30.75, -97.48], zoom=10, children=[
                             dl.TileLayer(),
                             *geo_map
                         ])
    else:
        geo_map = "Error: Latitude or Longitude data missing"

    return table_data, pie_fig, geo_map

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




