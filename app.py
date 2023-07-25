from dash import Dash
import dash_bootstrap_components as dbc

from src.components.layout import create_layout


def init_app():
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
        meta_tags=[
            {
                "name": "viewport",
                "content": "width=device-width, initial-scale=1.0",
                "charset": "utf-8",
            }
        ],
    )
    app.title = "Netflix Viewing Activity Dashboard"
    app.layout = create_layout(app)
    return app


if __name__ == "__main__":
    app = init_app()
    app.run_server(debug=False)
