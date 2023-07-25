import pandas as pd


def load_viewing_activity_data(path):
    viewing_activity_data = pd.read_csv(
        path,
        dtype={
            "Profile Name": str,
            "Start Time": str,
            "Duration": str,
            "Title": str,
        },
    )

    return preprocess_viewing_activity_data(viewing_activity_data)


def preprocess_viewing_activity_data(viewing_activity_data):
    viewing_activity_data["Title"] = viewing_activity_data["Title"].apply(
        preprocess_title_col
    )

    viewing_activity_data["Start Time"] = pd.to_datetime(
        viewing_activity_data["Start Time"], utc=True
    )

    viewing_activity_data["Year"] = viewing_activity_data["Start Time"].dt.year.astype(
        str
    )

    viewing_activity_data["Duration in Seconds"] = viewing_activity_data[
        "Duration"
    ].apply(convert_to_seconds)

    viewing_activity_data["Duration in Hours"] = viewing_activity_data[
        "Duration"
    ].apply(convert_to_hours)

    # Filter out short videos (less than 3 minutes)
    filt = viewing_activity_data["Duration in Seconds"] > 180
    viewing_activity_data = viewing_activity_data[filt]

    # Drop columns that are no longer needed
    viewing_activity_data = viewing_activity_data.drop(
        columns=["Duration", "Duration in Seconds"]
    )

    return viewing_activity_data


def preprocess_title_col(title_description):
    # Remove _hook from the end of the string
    title_description_list = title_description.split("_hook", 1)[0].split(":")

    if title_description_list[0].startswith("Season"):
        return title_description_list[1]

    return title_description_list[0]


def convert_to_seconds(duration):
    hours, minutes, seconds = [int(time_unit) for time_unit in duration.split(":")]
    return 3600 * hours + 60 * minutes + seconds


def convert_to_hours(duration):
    hours, minutes, seconds = [int(time_unit) for time_unit in duration.split(":")]
    return round(hours + minutes / 60 + seconds / 3600, 2)
