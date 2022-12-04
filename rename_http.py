# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:47:22 2022
@author: lenka
"""

import pandas as pd
import os
import json


for i in range(21, 40):
    file = open('data/out' + str(i) + '.json')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)
    
    instance = str(data_nor['metric.instance'])[5:22].replace(":", "_")
    instance = instance.replace(".", "_")
    
    consumer = str(data_nor['metric.consumer'])[5:21]
    route = str(data_nor['metric.route'])[5:16]
    
    code = str(data_nor['metric.code'])[5:8]

    print(instance, consumer, route)
    old_name = ('data/out' + str(i) + '.json')
    new_name = ('data/out' + "_"+str(instance) + "_" + str(consumer)+"_" + str(route)+"_" + str(code) + '.json')
    file.close()
    os.rename(old_name, new_name)
