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
                            className="img-fluid rounded mx-auto d-block mw-25 h-auto",
                        ),
                        width=12,
                    ),
                    dbc.Col(
                        html.H1(
                            app.title,
                            className="text-capitilize text-center mb-2 fs-3",
                        ),
                        width=12,
                    ),
                    dbc.Col(
                        html.P(
                            children=[
                                "This dashboard is a data visualization of my Netflix viewing activity data. ",
                                "The data is collected from Netflix's viewing activity page. ",
                                "Then, the data is preprocessed and visualized using Python, Pandas, and Dash. ",
                                html.Br(),
                                html.Br(),
                                "I am aware that I do not have that much data, because I have just started using Netflix. ",
                                "Because of this, I added some fake data to make the graphs look more interesting. ",
                                "However, this code should work for any amount of data. ",
                                "This will be removed in the future, after I have sufficient data. ",
                                "Additionally, I tried to make the dashboard layout as responsive as possible. ",
                                "Please do not judge my preferences 😊",
                            ],
                            className="mb-4 fs-6 mx-auto text-center",
                        ),
                        xs=12,
                        sm=12,
                        md=9,
                        lg=8,
                        xl=6,
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
                className="mb-4",
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
