from matplotlib import cm
import matplotlib.pyplot as plt
import pytz
import numpy as np
from datetime import date, datetime
import pandas as pd


def add_lines(df, color, label, ax, dk_start_time, linewidth):
    df['datetime'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
    df['datetime'] = df['datetime'].apply(lambda t: datetime.combine(
        date.today(), t).replace(tzinfo=pytz.timezone('Europe/Copenhagen')))
    df['x'] = (df['datetime'] - dk_start_time).dt.total_seconds()
    ax.plot(df['x'], df['KWH'], label=label, linewidth=linewidth, color=color)


def plot_data(df, title):

    avg_kwh_df = df.groupby('time')['KWH'].mean().reset_index()
    # Determine the current date
    current_date = datetime.now().date()

    # Calculate the number of days since each date in the data
    df['date'] = df['x'].dt.date
    df['days_since_today'] = df['date'].apply(
        lambda x: (current_date - x).days)

    # Define a colormap
    cmap = cm.get_cmap('Blues')

    fig, ax = plt.subplots()

    today_date = datetime.now().date()
    today_data = df.loc[df['date'] == today_date]

    for i, (date, date_data) in enumerate(df.groupby('date')):
        start_time = datetime.combine(date, datetime.min.time())
        dk_timezone = pytz.timezone('Europe/Copenhagen')
        dk_start_time = dk_timezone.localize(start_time)
        filtered_data = date_data.copy()
        filtered_data['x'] = (filtered_data['x'] -
                              dk_start_time).dt.total_seconds()

        start_time = 0

        x_max = 86400
        # Update x-axis ticks and labels
        x_ticks = np.linspace(start_time, x_max)
        ax.set_xticks(x_ticks)
        x_tick_labels = pd.to_datetime(x_ticks, unit='s').strftime('%H:%M')
        ax.set_xticklabels(x_tick_labels)

        if date == today_date:
            # Use green for today's date
            color = 'green'
            newlinewidth = 4
        else:
            # Use cmap for other dates
            color = cmap(i / (len(df.groupby('date')) - 1))
            newlinewidth = 2

        ax.plot(filtered_data['x'], filtered_data['KWH'],
                alpha=1, label=date.strftime("%Y-%m-%d"), color=color, linewidth=newlinewidth)

    add_lines(avg_kwh_df, 'red', 'Gennemsnit', ax, dk_start_time, 2)

    # print(df)
    plt.xlabel("Klokken")
    plt.ylabel("KwP/Procent")
    plt.title(title + " pr. dag")
    plt.legend()
