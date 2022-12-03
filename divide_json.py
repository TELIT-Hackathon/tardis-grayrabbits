# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:47:22 2022

@author: lenka
"""


import pandas as pd
import json
import os
import json

'''
with open('http_status.json') as user_file:
    content = user_file.read()

test = ""
j = 0
for i in range(0, 100000):
    if content[i] != "}":
        test += content[i]
      
    else: 
        test += content[i]
        with open('data'+str(j) + '.json', 'w') as f:
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
            j += 1
            test = ""
'''

# prepare control variables
i = 0
file_in = open('bandwidth.json')
# start reading big json
while True:
    # iterator: helps to name the files
    i += 1
    primed = False
    # get first character into buffer
    char = file_in.read(1)
    # create smaller file
    file_out = open('out' + i + '.json', 'w')
    while True:
        file_out.write(char)
        if char == ']':
            primed = True
        elif char == '}' and primed:
            file_out.write('}')
            break
        else:
            primed = False
    # close the created file
    file_out.close()
    # end of file is reached
    if char is None:
        break
file_in.close()