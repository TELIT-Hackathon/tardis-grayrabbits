import numpy as np
import json
import pandas as pd
from matplotlib import pyplot as plt
import datetime


for i in range(1, 20):
    file = open('data/out' + str(i) + '.json')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)

    data_val = data_nor['metric.values'][0]
    data_time = data_nor['metric.timestamps'][0]

    for j in range(len(data_time)):
        data_time[j] = datetime.datetime.fromtimestamp(data_time[j]/1000)

    x = np.array(data_time)
    y = np.array(data_val)
    plt.title(str(data_nor['metric.code'][0]))
    plt.xlabel("timestamps")
    plt.ylabel("values")
    plt.plot(x, y)
    plt.show()