import matplotlib.pyplot as plt
import api_data as apidata
import data_formatting as formatdata
import plot_data as plotdata
import datapunkter


data_telemetry = apidata.get_data()

for i, field in datapunkter.TELEMETRY_FIELDS.items():
    print(field)
    name = field["name"]
    human_text = field["human_text"]
    df = formatdata.format_data(data_telemetry, name)
    plotdata.plot_data(df, human_text)


plt.show()
