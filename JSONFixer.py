import json
import chardet
import pandas as pd

"""
f =  open('data/http_status.json', 'rb', encoding='ascii')
    enc = chardet.detect(f.read())  # or readline if the file is large
    print(enc)
"""
"""
f = open('data/http_status.json', 'r', encoding='ascii')

data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
    print(i)

# Closing file
f.close()
"""

inputFile = open('http_status.json', 'r', encoding='ascii', buffering=100000000)

outputFile = open("http_statusFixed.json", "ab", buffering=100000000)
outputFile.write("{\n\"samples\":\n[".encode('ascii'))
endSample = False
for line in inputFile:
    if endSample:
        endSample = False
        outputFile.write("},\n".encode('ascii'))

    outputFile.write(line.encode('ascii'))
    length = len(line)
    if line[length - 1 - 1] == '}':
        endSample = True
        
outputFile.write("\n}\n]\n}\n".encode('ascii'))

outputFile.close()

inputFile.close()

f = open('http_statusFixed.json', 'r', encoding='ascii')

data = json.load(f)
