import json
import pandas as pd
from sklearn import preprocessing as prep

'''
for i in range(1, 51):
    file = open('data_https/out' + str(i) + '.json')
    file_out = open('data_https/new' + str(i) + '.json', 'w')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)
    data_time = data_nor['metric.timestamps'][0]
    data_val = data_nor['metric.values'][0]
    data_val = prep.minmax_scale(data_val, feature_range=(0, 100))

    file_out.write('{\n"timeseries": [\n')
    for j in range(len(data_val) - 1):
        file_out.write('{ "value": ' + str(data_val[j]))
        file_out.write(', "time": ' + str(data_time[j]) + ' },\n')
    file_out.write('{ "value": ' + str(data_val[len(data_val) - 1]))
    file_out.write(', "time": ' + str(data_time[len(data_val) - 1]) + ' }\n]}')
'''

file_avg = open('data_https/avg.json', 'w')
filenames = ['data_https/out7.json', 'data_https/out2.json', 'data_https/out15.json']
file = open(filenames[0])
data1 = json.loads(file.read())
data_nor1 = pd.json_normalize(data1)
data_val1 = data_nor1['metric.values'][0]
data_val1 = prep.minmax_scale(data_val1, feature_range=(0, 100))
file = open(filenames[1])
data2 = json.loads(file.read())
data_nor2 = pd.json_normalize(data2)
data_val2 = data_nor2['metric.values'][0]
data_val2 = prep.minmax_scale(data_val2, feature_range=(0, 100))
file = open(filenames[2])
data3 = json.loads(file.read())
data_nor3 = pd.json_normalize(data3)
data_val3 = data_nor3['metric.values'][0]
data_val3 = prep.minmax_scale(data_val3, feature_range=(0, 100))

data_time = data_nor1['metric.timestamps'][0]
file_avg.write('{\n"timeseries": [\n')
for i in range(len(data_time) - 1):
    file_avg.write('{ "time": ' + str(data_time[i]) + ', ')
    file_avg.write('"value1": ' + str(data_val1[i]) + ', ')
    file_avg.write('"value2": ' + str(data_val2[i]) + ', ')
    file_avg.write('"value3": ' + str(data_val3[i]) + ' },\n')
file_avg.write('{ "time": ' + str(data_time[len(data_time) - 1]) + ', ')
file_avg.write('"value1": ' + str(data_val1[len(data_time) - 1]) + ', ')
file_avg.write('"value2": ' + str(data_val2[len(data_time) - 1]) + ', ')
file_avg.write('"value3": ' + str(data_val3[len(data_time) - 1]) + ' }\n]}')
