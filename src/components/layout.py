from dash import html, dcc
import dash_bootstrap_components as dbc

from . import card_group
from . import dropdowns
from . import ids
from . import chart


def create_layout(app):
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            src=app.get_asset_url("netflix_logo.png"),
                            style={
                                "width": "100%",
                                "max-width": "285px",
                                "position": "relative",
                                "left": "50%",
                                "transform": "translate(-50%, 0)",
                            },
                        ),
                        width=12,
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                children=[
                                    html.H1(
                                        app.title,
                                        className="text-capitalize fs-2 mb-6",
                                    ),
                                    html.P(
                                        children=[
                                            "This dashboard is a data visualization of my Netflix viewing activity data. ",
                                            "The data is collected from Netflix's viewing activity page. ",
                                            "Then, the data is preprocessed and visualized using Python, Pandas, and Dash. ",
                                            html.Br(),
                                            html.Br(),
                                            "I am aware that I do not have that much data because I have just started using Netflix. ",
                                            "Because of this, I added some example data to make the graphs look more interesting. ",
                                            "However, this code should work for any amount of data. ",
                                            "This will be removed in the future after I have sufficient data. ",
                                            "Additionally, I tried to make the dashboard layout as responsive as possible. ",
                                            "Please do not judge my preferences 😊",
                                        ],
                                        className="fs-6",
                                        style={
                                            "width": "0",
                                            "min-width": "100%",
                                            "text-align": "justify",
                                            "text-justify": "inter-word",
                                        },
                                    ),
                                ],
                                className="mb-2",
                                style={
                                    "display": "inline-block",
                                    "vertical-align": "middle",
                                    "position": "relative",
                                    "left": "50%",
                                    "transform": "translate(-50%, 0)",
                                },
                            )
                        ],
                        xs=11,
                        sm=11,
                    ),
                ],
                justify="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        card_group.create_card_group(),
                        className="text-center",
                    )
                ],
                className="mb-3",
                justify="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardGroup(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H3(
                                                "Select Graph to Display",
                                                className="fs-6",
                                            ),
                                            dropdowns.render_chart_dropdown(),
                                        ]
                                    ),
                                    className="m-2",
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H3(
                                                "Select Year(s) to Filter Data",
                                                className="fs-6",
                                            ),
                                            dropdowns.render_years_dropdown(),
                                        ]
                                    ),
                                    className="m-2",
                                ),
                            ],
                            class_name="text-white mb-2",
                        )
                    )
                ],
                justify="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(
                            id=ids.DATA_CHART,
                            figure=chart.render_top_10_most_viewed_titles_fig(),
                            responsive=True,
                            className="ms-2 me-2",
                        ),
                        width=12,
                    )
                ],
                justify="center",
            ),
        ],
        fluid=True,
    )
