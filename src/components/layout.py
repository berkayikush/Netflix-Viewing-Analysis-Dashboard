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
                                            "This dashboard presents the visualization of my ",
                                            "Netflix viewing activity data, collected from Netflix's viewing activity page. ",
                                            "The data is collected from Netflix's viewing activity page. ",
                                            "The data undergoes preprocessing and is then visualized using Python, Pandas, Plotly, and Dash. ",
                                            "The code is designed to be flexible and capable of handling any amount of data. ",
                                            "I've put effort into making the dashboard layout as responsive as possible. ",
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
