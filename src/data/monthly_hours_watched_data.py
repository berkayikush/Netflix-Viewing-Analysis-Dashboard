import pandas as pd


def create_monthly_hours_watched_data(viewing_activity_data):
    monthly_hours_watched_data = viewing_activity_data.copy()
    monthly_hours_watched_data["Month"] = (
        monthly_hours_watched_data["Start Time"].sort_values().dt.month
    )

    monthly_hours_watched_data = (
        monthly_hours_watched_data.groupby(["Month", "Year"], as_index=False)[
            "Duration in Hours"
        ]
        .sum()
        .sort_values("Year")
    )

    monthly_hours_watched_data = add_missing_months_for_years_before_curr(
        monthly_hours_watched_data
    )

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


def add_missing_months_for_years_before_curr(monthly_hours_watched_data):
    filtered_years = monthly_hours_watched_data["Year"].unique()[
        : len(monthly_hours_watched_data["Year"].unique()) - 1
    ]

    for year in filtered_years:
        for month in range(1, 13):
            if not monthly_hours_watched_data[
                (monthly_hours_watched_data["Year"] == year)
                & (monthly_hours_watched_data["Month"] == month)
            ].any()["Month"]:
                new_row = {"Month": month, "Year": year, "Duration in Hours": 0}
                monthly_hours_watched_data = pd.concat(
                    [monthly_hours_watched_data, pd.DataFrame([new_row])],
                    ignore_index=True,
                )

    return monthly_hours_watched_data.sort_values(["Month", "Year"])
