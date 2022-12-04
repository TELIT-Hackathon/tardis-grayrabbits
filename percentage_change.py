import numpy as np
import json
import pandas as pd
from matplotlib import pyplot as plt
import datetime

x = []
y = []
for i in range(100,110):
    file = open('data/out' + str(i) + '.json')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)
    total_change = data_nor['metric.values'][0][1439]-data_nor['metric.values'][0][0]
    print("total change", total_change )
    
    data_val = data_nor['metric.values'][0]
    data_time = data_nor['metric.timestamps'][0]
    if total_change !=0:
        data_change = [0]*40
    else:
        data_change = [0]*1440
    for j in range(0,len(data_time)):
        data_time[j] = datetime.datetime.fromtimestamp(data_time[j]/1000)
        if j>20 and total_change != 0 and j%20==0:
            for k in range(0,20):
                data_change.append(((data_nor['metric.values'][0][j]-data_nor['metric.values'][0][j-20])/total_change)*100)
                

    print(i)
    x.append(np.array(data_time))
    y.append(np.array(data_change))
    #plt.title(str(data_nor['metric.code'][0]))
    plt.xlabel("timestamps")
    plt.ylabel("data_change %")
    plt.plot(x, y)
    
plt.show()