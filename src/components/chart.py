from dash import Input, Output, callback
import plotly.express as px

from . import ids
from ..data.netflix_analysis_data import NetflixAnalysisData

COLOR_SCHEME = ["#940404", "#c62222", "#e74c3c", "#ff7f7f", "#ffaaaa"]


@callback(
    Output(ids.DATA_CHART, "figure"),
    Input(ids.DATA_CHART_DROPDOWN, "value"),
    Input(ids.YEARS_DROPDOWN, "value"),
)
def update_data_chart(filtered_chart, filtered_years):
    fig = None

    match filtered_chart:
        case "Top 10 Most Viewed Titles Graph":
            mask = NetflixAnalysisData.TOP_10_MOST_VIEWED_TITLES["Year"].isin(
                filtered_years
            )
            filtered_data = NetflixAnalysisData.TOP_10_MOST_VIEWED_TITLES[mask]
            fig = render_top_10_most_viewed_titles_fig(filtered_data)

        case "Hours Watched for Each Day of the Week Graph":
            mask = NetflixAnalysisData.HOURS_WATCHED_PER_DAY["Year"].isin(
                filtered_years
            )
            filtered_data = NetflixAnalysisData.HOURS_WATCHED_PER_DAY[mask]
            fig = render_hours_watched_per_day_fig(filtered_data)

        case "Monthly Hours Watched Graph":
            mask = NetflixAnalysisData.MONTHLY_HOURS_WATCHED["Year"].isin(
                filtered_years
            )
            filtered_data = NetflixAnalysisData.MONTHLY_HOURS_WATCHED[mask]
            fig = render_monthly_hours_watched_fig(filtered_data)

    return fig


def render_top_10_most_viewed_titles_fig(
    data=NetflixAnalysisData.TOP_10_MOST_VIEWED_TITLES,
):
    fig = px.bar(
        data,
        x="Duration in Hours",
        y="Title",
        color="Year",
        title="Top 10 Most Viewed Titles Over the Years",
        labels={
            "Duration in Hours": "hours watched",
            "Title": "title",
            "Year": "year",
        },
        category_orders={"Year": sorted(set(data["Year"].tolist()), key=int)},
        orientation="h",
        opacity=0.8,
        template="plotly_dark",
        color_discrete_sequence=COLOR_SCHEME,
        barmode="relative",
        text_auto=True,
    )
    fig.update_layout(
        xaxis={"fixedrange": True},
        yaxis={"categoryorder": "total ascending", "fixedrange": True},
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},
        autosize=True,
    )
    fig.update_yaxes(automargin=True)
    fig.update_xaxes(automargin=True)

    return fig


def render_hours_watched_per_day_fig(
    data=NetflixAnalysisData.HOURS_WATCHED_PER_DAY,
):
    fig = px.bar(
        data,
        x="Duration in Hours",
        y="Day Name",
        color="Year",
        title="Hours Watched for Each Day of the Week Over the Years",
        labels={
            "Duration in Hours": "hours watched",
            "Day Name": "day",
            "Year": "year",
        },
        category_orders={"Year": sorted(set(data["Year"].tolist()), key=int)},
        orientation="h",
        opacity=0.8,
        template="plotly_dark",
        color_discrete_sequence=COLOR_SCHEME,
        text_auto=True,
    )
    fig.update_layout(
        xaxis={"fixedrange": True},
        yaxis={"categoryorder": "total ascending", "fixedrange": True},
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},
        autosize=True,
    )
    fig.update_yaxes(automargin=True)
    fig.update_xaxes(automargin=True)

    return fig


def render_monthly_hours_watched_fig(
    data=NetflixAnalysisData.MONTHLY_HOURS_WATCHED,
):
    fig = px.line(
        data,
        x="Month",
        y="Duration in Hours",
        color="Year",
        title="Monthly Hours Watched Over the Years",
        labels={
            "Month": "month",
            "Duration in Hours": "hours watched",
            "Year": "year",
        },
        template="plotly_dark",
        color_discrete_sequence=COLOR_SCHEME,
    )
    fig.update_layout(
        xaxis={"fixedrange": True},
        yaxis={"fixedrange": True},
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},
        autosize=True,
    )
    fig.update_traces(line={"width": 3.5})
    fig.update_yaxes(automargin=True)
    fig.update_xaxes(automargin=True)

    return fig
