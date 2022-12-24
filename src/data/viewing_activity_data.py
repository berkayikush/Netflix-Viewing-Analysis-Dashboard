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

    # Since currently I do not have much data, I added some example data to make the graphs look more interesting.
    # This will be removed in the future, after I have sufficient data.
    viewing_activity_data = pd.concat(
        [viewing_activity_data, create_example_data()],
        ignore_index=True,
    )

    return viewing_activity_data


def preprocess_title_col(title_description):
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


def create_example_data():
    example_data = {
        "Profile Name": ["Berkay"] * 12,
        "Start Time": [
            pd.to_datetime("2021-01-10 20:33:04+00:00", utc=True),
            pd.to_datetime("2021-02-5 16:29:04+00:00", utc=True),
            pd.to_datetime("2021-03-23 12:10:04+00:00", utc=True),
            pd.to_datetime("2021-04-16 12:25:04+00:00", utc=True),
            pd.to_datetime("2021-05-3 23:16:04+00:00", utc=True),
            pd.to_datetime("2021-06-7 22:13:04+00:00", utc=True),
            pd.to_datetime("2021-07-27 07:12:04+00:00", utc=True),
            pd.to_datetime("2021-08-21 09:45:04+00:00", utc=True),
            pd.to_datetime("2021-09-13 10:53:04+00:00", utc=True),
            pd.to_datetime("2021-10-17 11:18:04+00:00", utc=True),
            pd.to_datetime("2021-11-14 11:32:04+00:00", utc=True),
            pd.to_datetime("2021-12-8 09:45:04+00:00", utc=True),
        ],
        "Title": [
            "BoJack Horseman",
            "Black Mirror",
            "Black Mirror",
            "Stranger Things",
            "Stranger Things",
            "Breaking Bad",
            "Breaking Bad",
            "Stranger Things",
            "The Office",
            "The Office",
            "The Office",
            "Elite",
        ],
        "Year": ["2021"] * 12,
        "Duration in Hours": [
            3.2,
            2.5,
            2.3,
            2.1,
            2.0,
            1.9,
            1.8,
            1.7,
            1.6,
            1.5,
            1.4,
            3.4,
        ],
    }

    return pd.DataFrame.from_dict(example_data)
