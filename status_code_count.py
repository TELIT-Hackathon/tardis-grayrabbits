# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:47:22 2022
@author: lenka
"""

import pandas as pd
import json
import os
import json
data_code = []

for i in range(100, 1000):
    file = open('data/out' + str(i) + '.json')
    data = json.loads(file.read())
    data_nor = pd.json_normalize(data)
    data_code.append(data_nor['metric.code'][0])

    
# print("202 ", data_code.count("202"))
# print("201 ", data_code.count("201"))
# print("204 ", data_code.count("204"))
# print("206 ", data_code.count("206"))
# print("210 ", data_code.count("210"))
# print("302 ", data_code.count("302"))
# print("200 ", data_code.count("200"))
# print("400 ", data_code.count("400"))
# print("401 " , data_code.count("401"))
# print("403 ", data_code.count("403"))
# print("404 ", data_code.count("404"))
# print("500 ", data_code.count("500"))
# print("503 ", data_code.count("503"))
# print("504 ", data_code.count("504"))



code_count=[]

codes = [202, 201, 204,206, 210,302,200, 400, 401, 403, 404, 500, 503, 504]
i = 0
print(codes[i])
print(data_code.count(str(codes[i])))
      
file_out = open('code_counts.json', 'w')
file_out.write('{\n "codes": [ \n')

for i in range(len(codes)):
    file_out.write('{"' + str(codes[i]) + '" :' + str(data_code.count(str(codes[i]))) +'}, \n')
    print(str(codes[i]) + " " +str(data_code.count(str(codes[i])) ))
file_out.write(']\n }')

file_out.close()

