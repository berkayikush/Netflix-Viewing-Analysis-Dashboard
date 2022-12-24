def create_daily_hours_watched_data(viewing_activity_data):
    daily_hours_watched_data = viewing_activity_data.copy()
    daily_hours_watched_data["Day"] = daily_hours_watched_data[
        "Start Time"
    ].dt.day_name()

    return (
        daily_hours_watched_data.groupby(["Day", "Year"], as_index=False)[
            "Duration in Hours"
        ]
        .sum()
        .sort_values("Duration in Hours", ascending=False)
    )
