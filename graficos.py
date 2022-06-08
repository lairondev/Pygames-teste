from dash import Dash
from dash_html_components import H1, Div, P
from dash_core_components import Graph

app = Dash(__name__)

app.layout = Div(
    children = [
        H1("Olá mundo!"),
        P("Trabalhando com Python Web"),
        Graph(
            figure = {
                "data": [
                    {"x": [0,25,50,75,100], "type": "box"},
                ],
                "layout": {
                
                }
            }
        )
    ]
)

app.run_server(debug=True)
