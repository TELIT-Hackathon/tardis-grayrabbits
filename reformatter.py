import json
import pandas as pd


for i in range(1, 51):
    file = open('data_https/out' + str(i) + '.json')
    file_out = open('data_https/new' + str(i) + '.json', 'w')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)
    data_time = data_nor['metric.timestamps'][0]
    data_val = data_nor['metric.values'][0]

    file_out.write('{\n"timeseries": [\n')
    for i in range(len(data_val) - 1):
        file_out.write('{ "value": ' + str(data_val[i]))
        file_out.write(', "time": ' + str(data_time[i]) + ' },\n')
    file_out.write('{ "value": ' + str(data_val[len(data_val) - 1]))
    file_out.write(', "time": ' + str(data_time[len(data_val) - 1]) + ' }\n]}')