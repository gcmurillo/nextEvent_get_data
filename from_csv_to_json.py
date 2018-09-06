
import csv
import json

csvfile = open('data.csv', 'r')
jsonfile = open('_data.json', 'w')

fieldnames = ("date","text","url_imagen","categoria")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write('[')
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',')
jsonfile.write(']')
