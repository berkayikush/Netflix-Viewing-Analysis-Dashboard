def create_top_10_most_viewed_titles_data(viewing_activity_data):
    return (
        viewing_activity_data.groupby(["Title", "Year"], as_index=False)[
            "Duration in Hours"
        ]
        .sum()
        .sort_values("Duration in Hours", ascending=False)
        .head(10)
    )
