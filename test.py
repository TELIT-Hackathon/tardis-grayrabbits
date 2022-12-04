import numpy as np
import json
import pandas as pd
from matplotlib import pyplot as plt
import datetime
from sklearn import preprocessing as prep


for i in range(1, 20):
    filename1 = ('data_https/out' + str(i) + '.json')
    filename2 = ('data_bandwidth/out' + str(i) + '.json')
    file1 = open(filename1)
    file2 = open(filename2)
    data1 = json.loads(file1.read())
    data_nor1 = pd.json_normalize(data1)
    data2 = json.loads(file2.read())
    data_nor2 = pd.json_normalize(data2)

    data_val1 = data_nor1['metric.values'][0]
    data_time1 = data_nor1['metric.timestamps'][0]
    data_val2 = data_nor2['metric.values'][0]
    data_time2 = data_nor2['metric.timestamps'][0]

    for j in range(len(data_time1)):
        data_time1[j] = datetime.datetime.fromtimestamp(data_time1[j]/1000)
        data_time2[j] = datetime.datetime.fromtimestamp(data_time2[j]/1000)

    x = np.array(data_time1)
    data_val1 = np.array(data_val1)
    y = prep.minmax_scale(data_val1, feature_range=(0, 10))
    plt.title(data_nor1['metric.code'][0] + ' - ' + filename1)
    plt.xlabel("timestamps")
    plt.ylabel("values")
    plt.plot(x, y)
    data_val2 = np.array(data_val2)
    y = prep.minmax_scale(data_val2, feature_range=(0, 10))
    plt.xlabel("timestamps")
    plt.ylabel("values")
    plt.plot(x, y)
    plt.show()
'''

file = open('data_https/out1.json')
file_out = open('data_https/new1.json', 'w')
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
'''
