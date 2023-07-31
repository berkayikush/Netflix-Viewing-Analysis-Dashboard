from dash import html
import dash_bootstrap_components as dbc

from ..data.netflix_analysis_data import NetflixAnalysisData


def create_card_group():
    most_viewed_title = NetflixAnalysisData.MOST_VIEWED_TITLES.iloc[0]["Title"]

    avg_num_hours_watched_per_day = calculate_avg_num_hours_watched_per_day(
        NetflixAnalysisData.VIEWING_ACTIVITY
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


def calculate_avg_num_hours_watched_per_day(viewing_activity_data):
    daily_watch_duration = viewing_activity_data.groupby(
        viewing_activity_data["Start Time"].dt.date
    )["Duration in Hours"].sum()

    return daily_watch_duration.mean()


def create_most_viewed_title_card(most_viewed_title):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H3(children=[html.I(className="bi bi-heart-fill fs-5")]),
                html.H3("Most viewed title", className="fs-6"),
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
                html.H3("Daily hours watched on average", className="fs-6"),
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
                html.H3("Yearly hours watched on average", className="fs-6"),
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
                html.H3("Most active year", className="fs-6"),
                html.P(
                    f"{most_viewed_year}",
                    className="text-danger",
                ),
            ],
            className="border-start border-5 border-danger",
        ),
        class_name="m-2",
    )
