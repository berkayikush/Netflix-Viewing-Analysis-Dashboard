from dash import html
import dash_bootstrap_components as dbc

from ..data.netflix_analysis_data import NetflixAnalysisData


def create_card_group():
    most_viewed_title = NetflixAnalysisData.TOP_10_MOST_VIEWED_TITLES["Title"].iloc[0]
    avg_num_hours_watched_per_day = (
        NetflixAnalysisData.DAILY_HOURS_WATCHED.groupby("Day")["Duration in Hours"]
        .sum()
        .mean()
    )

    avg_num_hours_watched_per_year = (
        NetflixAnalysisData.VIEWING_ACTIVITY.groupby("Year")["Duration in Hours"]
        .sum()
        .mean()
    )
    most_viewed_year = (
        NetflixAnalysisData.VIEWING_ACTIVITY.groupby("Year")["Duration in Hours"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    return dbc.CardGroup(
        [
            create_most_viewed_title_card(most_viewed_title),
            create_avg_num_hours_watched_per_day_card(avg_num_hours_watched_per_day),
            create_avg_num_hours_watched_per_year_card(avg_num_hours_watched_per_year),
            create_most_viewed_year_card(most_viewed_year),
        ],
        className="text-white",
    )


def create_most_viewed_title_card(most_viewed_title):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H3(children=[html.I(className="bi bi-heart-fill fs-5")]),
                html.H3("The most viewed title", className="fs-6"),
                html.P(
                    f"{most_viewed_title}",
                    className="text-danger",
                ),
            ],
            className="border-start border-5 border-danger",
        ),
        class_name="m-2",
    )


def create_avg_num_hours_watched_per_day_card(avg_num_hours_watched_per_day):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H3(children=[html.I(className="bi bi-clock-fill fs-5")]),
                html.H3(
                    "The average number of hours watched per day", className="fs-6"
                ),
                html.P(
                    f"{avg_num_hours_watched_per_day:.2f}",
                    className="text-danger",
                ),
            ],
            className="border-start border-5 border-danger",
        ),
        class_name="m-2",
    )


def create_avg_num_hours_watched_per_year_card(avg_num_hours_watched_per_year):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H3(children=[html.I(className="bi bi-laptop-fill fs-5")]),
                html.H3(
                    "The average number of hours watched per year", className="fs-6"
                ),
                html.P(
                    f"{avg_num_hours_watched_per_year:.2f}",
                    className="text-danger",
                ),
            ],
            className="border-start border-5 border-danger",
        ),
        class_name="m-2",
    )


def create_most_viewed_year_card(most_viewed_year):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H3(children=[html.I(className="bi bi-calendar-fill fs-5")]),
                html.H3("The most viewed year", className="fs-6"),
                html.P(
                    f"{most_viewed_year}",
                    className="text-danger",
                ),
            ],
            className="border-start border-5 border-danger",
        ),
        class_name="m-2",
    )
