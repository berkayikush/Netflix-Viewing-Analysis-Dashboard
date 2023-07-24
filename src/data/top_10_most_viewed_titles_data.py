def create_top_10_most_viewed_titles_data(viewing_activity_data):
    top_10_viewed_titles = (
        viewing_activity_data.groupby(["Title"], as_index=False)["Duration in Hours"]
        .sum()
        .sort_values("Duration in Hours", ascending=False)
        .head(10)
    )["Title"]

    top_10_most_viewed_titles_over_years_data = viewing_activity_data.groupby(
        ["Title", "Year"], as_index=False
    )["Duration in Hours"].sum()

    # Drop the rows where duration is less than 0.5.
    top_10_most_viewed_titles_over_years_data = (
        top_10_most_viewed_titles_over_years_data[
            top_10_most_viewed_titles_over_years_data["Duration in Hours"] > 0.5
        ]
    )

    mask = top_10_most_viewed_titles_over_years_data["Title"].isin(top_10_viewed_titles)
    return top_10_most_viewed_titles_over_years_data.loc[mask]
