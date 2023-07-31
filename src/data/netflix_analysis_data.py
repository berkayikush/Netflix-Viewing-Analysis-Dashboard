from .viewing_activity_data import load_viewing_activity_data
from .most_viewed_titles_data import create_most_viewed_titles_data
from .hours_watched_per_day_data import create_hours_watched_per_day_data
from .monthly_hours_watched_data import create_monthly_hours_watched_data

DATA_PATH = "csv_data/ViewingActivity.csv"


class NetflixAnalysisData:
    VIEWING_ACTIVITY = load_viewing_activity_data(DATA_PATH)
    MOST_VIEWED_TITLES = create_most_viewed_titles_data(VIEWING_ACTIVITY)
    HOURS_WATCHED_PER_DAY = create_hours_watched_per_day_data(VIEWING_ACTIVITY)
    MONTHLY_HOURS_WATCHED = create_monthly_hours_watched_data(VIEWING_ACTIVITY)
