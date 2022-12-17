# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    dbc.Nav(
        [
            dbc.NavLink(
                [
                    html.Div(page["name"], className="ms-2"),
                ],
                href=page["path"],
                active="exact",
            )
            for page in dash.page_registry.values()
        ],
        fill=True,
        pills=True
    ),
    dbc.Container([
        dash.page_container
    ],
    fluid=True)
])

if __name__ == '__main__':
    app.run_server(debug=True)
