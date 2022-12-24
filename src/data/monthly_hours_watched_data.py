def create_monthly_hours_watched_data(viewing_activity_data):
    monthly_hours_watched_data = viewing_activity_data.copy()
    monthly_hours_watched_data["Month"] = (
        monthly_hours_watched_data["Start Time"].sort_values().dt.month
    )

    monthly_hours_watched_data = monthly_hours_watched_data.groupby(
        ["Month", "Year"], as_index=False
    )["Duration in Hours"].sum()

    # Replace the month numbers with their names
    monthly_hours_watched_data["Month"] = monthly_hours_watched_data["Month"].replace(
        {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
    )

    return monthly_hours_watched_data
