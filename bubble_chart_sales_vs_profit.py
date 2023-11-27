import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
data = pd.read_excel("C:/Users/Chandru/OneDrive/Desktop/Python Visuals/Sample - Superstore.xls", sheet_name="Orders")

# Create a Dash application
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': category, 'value': category} for category in data['Category'].unique()],
        value=data['Category'].unique(),
        multi=True
    ),
    dcc.Dropdown(
        id='sub-category-dropdown',
        options=[{'label': sub_category, 'value': sub_category} for sub_category in data['Sub-Category'].unique()],
        value=data['Sub-Category'].unique(),
        multi=True
    ),
    dcc.Graph(id='bubble-chart')
])

# Define callback to update graph
@app.callback(
    Output('bubble-chart', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('sub-category-dropdown', 'value')]
)
def update_graph(selected_categories, selected_sub_categories):
    filtered_data = data[data['Category'].isin(selected_categories) & data['Sub-Category'].isin(selected_sub_categories)]
    fig = px.scatter(filtered_data, x='Sales', y='Profit', size='Quantity', color='Category',
                     hover_data=['Product Name'], title='Product Sales vs. Profit')
    fig.update_layout(transition_duration=500)
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
