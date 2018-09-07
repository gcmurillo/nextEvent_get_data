import json
import requests
import csv

def procesarRequests(response,ciudad):
	data_str = response.json().get('events')
	jsons = json.dumps(data_str)
	json_data = json.loads(jsons)
	f = open("dataFacebook.csv", "w")
	for x in json_data['data']:
		try:
			if x["place"]["location"]["city"] == ciudad:
				try:
					date = x["start_time"]
				except:
					date = " "
				try:
					text = x["name"]
				except:
					text = " "
				try:
					categoria = " "
				except:
					categoria = " "
				linea = date+',"'+text+'",'+''+','+categoria+'\n'
				f.write(linea)
		except:
			pass
	f.close()



token = 'EAAfxCMZChZCTYBAEhqwmo5kkMAtxAyCzXhhdKjCe4A3TYDZCaMzO79LwexKD6ZATmXkK8YX1cAgMDUpAKT2vj2WuTDnRZCxDavFfbxzfg9toTQc9t7HOKMYNRwL6IBJwV8uo1qZBm4ZBd1nHe4ZAjVXIKeiHx44WO4bEVnVZAfTbfmgZDZD'
graph = 'https://graph.facebook.com/v3.1/'
text = '10211847728938977?fields=events{start_time,end_time,name,place,type,ticket_uri}&access_token='+token


link = graph + text

yo = requests.get(link)


if yo.status_code != 200:
    print('Falla en obtener datos:', yo.status_code)
else:
    procesarRequests(yo,"Guayaquil")
    #f.close()

