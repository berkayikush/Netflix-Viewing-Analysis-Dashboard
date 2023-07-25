from dash import dcc, html

from . import ids
from ..data.netflix_analysis_data import NetflixAnalysisData


def render_chart_dropdown():
    return dcc.Dropdown(
        [
            {
                "label": html.Span(
                    ["Top 10 Most Viewed Titles Graph"], className="text-primary"
                ),
                "value": "Top 10 Most Viewed Titles Graph",
                "search": "Top 10 Most Viewed Titles Graph",
            },
            {
                "label": html.Span(
                    ["Hours Watched for Each Day of the Week Graph"],
                    className="text-primary",
                ),
                "value": "Hours Watched for Each Day of the Week Graph",
                "search": "Hours Watched for Each Day of the Week Graph",
            },
            {
                "label": html.Span(
                    ["Monthly Hours Watched Graph"], className="text-primary"
                ),
                "value": "Monthly Hours Watched Graph",
                "search": "Monthly Hours Watched Graph",
            },
        ],
        id=ids.DATA_CHART_DROPDOWN,
        value="Top 10 Most Viewed Titles Graph",
        multi=False,
        clearable=False,
        optionHeight=50,
    )


def render_years_dropdown():
    unique_years = sorted(
        set(NetflixAnalysisData.VIEWING_ACTIVITY["Year"].tolist()), key=int
    )

    return dcc.Dropdown(
        id=ids.YEARS_DROPDOWN,
        options=[
            {"label": html.Span([year], className="text-primary"), "value": year}
            for year in unique_years
        ],
        value=unique_years,
        multi=True,
    )
