"""
Open the file using python
Read every line in the file
Output 1: Get list of unique airport names and number of times it is repeated in a json format
Output 2: Which airport is mentioned highest number of times and its count
Output 3: Which airport is mentioned lowest number of times and its count
Print the outputs

Input: csv file


Output1 :

{
"Atlanta, GA: Hartsfield-Jackson Atlanta International": 152,
"Baltimore, MD: Baltimore/Washington International Thurgood Marshall": 152
}
Output2: “Name and count of the airport which is mentioned the most number of time”

Output3: “Name and count of the airport which is mentioned the least number of time”
"""



import csv
import json

name_dict = {}
file = open(r"airlines.csv")
csv_f = csv.reader(file)
next(file)
for row in csv_f:
    code, name, year, cancel = row
    if name not in name_dict:
        name_dict[name] = 0
    name_dict[name] += 1

json_data = json.dumps(name_dict)
print(json_data)
max_val = max(name_dict, key=name_dict.get)
print(max_val, name_dict[max_val])
min_val = min(name_dict, key=name_dict.get)
print(min_val, name_dict[min_val])
