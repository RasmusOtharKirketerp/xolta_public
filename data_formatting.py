import pytz
from datetime import datetime
import pandas as pd
import datapunkter


def format_data(telemetry_data, datatype):
    x = []
    y = []
    for telemetry in telemetry_data:
        utc_end_time = telemetry["utcEndTime"]
        meter_kwh = telemetry[datatype]
        # print(meter_kwh, utc_end_time)
        if meter_kwh is not None:
            # Convert UTC End Time to datetime object
            utc_end_time = datetime.strptime(
                utc_end_time, "%Y-%m-%dT%H:%M:%SZ")
            utc_end_time = pytz.utc.localize(utc_end_time)
            dk_timezone = pytz.timezone('Europe/Copenhagen')
            dk_end_time = utc_end_time.astimezone(dk_timezone)
            x.append(dk_end_time)
            y.append(meter_kwh)

    # Create a Pandas dataframe with the telemetry data
    df = pd.DataFrame({"x": x, "KWH": y})

    # Add a 'date' column to the dataframe
    df['date'] = df['x'].dt.date
    df['time'] = df['x'].dt.time

    return df
