# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:47:22 2022

@author: lenka
"""


import pandas as pd
import json
import os


with open(r'/Users/lenka/Desktop/hackathon/http_status.json/http_status.json') as user_file:
  content = user_file.read()


import json


    
test = ""
j = 0
for i in range(0, 100000):
    if(content[i] != "}"):
        test += content[i]
      
    else: 
        test += content[i]
        with open('data'+str(j) +'.json', 'w') as f:
            original_String = test
            # import ast
            
            # # printing original string
            # print("The original string is : " + str(original_String))
            
            # # using ast.literal_eval() method
            # result = ast.literal_eval(original_String)
            
            # # print result
            # print("The converted dictionary is : " + str(result))
            # print(test)
            json.dump(test, f)
            j+= 1
            test = ""
