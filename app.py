# app.py
from flask import Flask, render_template
import api_data as apidata
import data_formatting as formatdata
import datapunkter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    data_telemetry = apidata.get_data()
    formatted_data = {}
    for i, field in datapunkter.TELEMETRY_FIELDS.items():
        name = field["name"]
        human_text = field["human_text"]
        df = formatdata.format_data(data_telemetry, name)
        formatted_data[human_text] = df.to_dict('list')

    return render_template('graph.html', datapunkter=datapunkter.TELEMETRY_FIELDS, data=formatted_data)


if __name__ == '__main__':
    app.run(debug=True)
