def create_hours_watched_per_day_data(viewing_activity_data):
    hours_watched_per_day_data = viewing_activity_data.copy()
    hours_watched_per_day_data["Day Name"] = hours_watched_per_day_data[
        "Start Time"
    ].dt.day_name()

    # Drop the rows where duration is less than 1.
    hours_watched_per_day_data = (
        hours_watched_per_day_data.groupby(["Day Name", "Year"], as_index=False)[
            "Duration in Hours"
        ]
        .sum()
        .sort_values("Duration in Hours", ascending=False)
    )

    # Drop the rows where duration is less than 0.5.
    hours_watched_per_day_data = hours_watched_per_day_data[
        hours_watched_per_day_data["Duration in Hours"] > 0.5
    ]

    return hours_watched_per_day_data
