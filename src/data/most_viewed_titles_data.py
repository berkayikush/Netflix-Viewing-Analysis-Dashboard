def create_most_viewed_titles_data(viewing_activity_data):
    most_viewed_titles_over_years_data = viewing_activity_data.groupby(
        ["Title", "Year"], as_index=False
    )["Duration in Hours"].sum()

    # Drop the rows where duration is less than 0.5.
    most_viewed_titles_over_years_data = most_viewed_titles_over_years_data[
        most_viewed_titles_over_years_data["Duration in Hours"] > 0.5
    ]

    print(
        most_viewed_titles_over_years_data.sort_values(
            "Duration in Hours", ascending=False
        )
    )
    return most_viewed_titles_over_years_data.sort_values(
        "Duration in Hours", ascending=False
    )
