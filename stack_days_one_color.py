import matplotlib.pyplot as plt
import api_data as apidata
import data_formatting as formatdata
import plot_data as plotdata
import datapunkter


data_telemetry = apidata.get_data()


def sanitize_filename(filename):
    return ''.join(c for c in filename if c.isalnum() or c == '_')


for i, field in datapunkter.TELEMETRY_FIELDS.items():
    print(field)
    name = field["name"]
    human_text = field["human_text"]
    df = formatdata.format_data(data_telemetry, name)
    plotdata.plot_data(df, human_text)

    filename = sanitize_filename(human_text) + '.png'
    plt.savefig(filename)

    filename = sanitize_filename(human_text) + '.csv'
    df.to_csv(filename)


plt.show()
