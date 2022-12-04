import numpy as np
import json
import pandas as pd
from matplotlib import pyplot as plt
import datetime

x = []
y = []
for i in range(1, 11):
    file = open('data_https/out' + str(i) + '.json')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)
    print("Consumer: " + data_nor['metric.consumer'][0])
    total_change = data_nor['metric.values'][0][1439]-data_nor['metric.values'][0][0]
    print("total change", total_change )
    
    data_val = data_nor['metric.values'][0]
    data_time = data_nor['metric.timestamps'][0]
    if total_change != 0:
        data_change = [0]*40
    else:
        data_change = [0]*1440
    for j in range(0, len(data_time)):
        if j > 20 and total_change != 0 and j % 20 == 0:
            for k in range(0, 20):
                data_change.append(((data_nor['metric.values'][0][j]-data_nor['metric.values'][0][j-20])/total_change) * 100)

    print(i)
    x.append(np.array(data_time))
    y.append(np.array(data_change))
    # plt.title(str(data_nor['metric.code'][0]))
    plt.xlabel("timestamps")
    plt.ylabel("data_change %")
    plt.plot(x, y)

# plt.show()

file_out = open('data_https/percentage.json', 'w')
file_out.write('{\n"timeseries": [\n')
for i in range(len(x[0]) - 1):
    file_out.write('{ "time": ' + str(x[0][i]) + ', ')
    for j in range(9):
        file_out.write('"value' + str(j) + '": ' + str(y[j][i]) + ', ')
    file_out.write('"value10": ' + str(y[9][i]) + ' },\n')
file_out.write('{ "time": ' + str(x[0][i]) + ', ')
for j in range(9):
    file_out.write('"value' + str(j) + '": ' + str(y[j][i]) + ', ')
file_out.write('"value10": ' + str(y[9][i]) + ' }\n]}')

