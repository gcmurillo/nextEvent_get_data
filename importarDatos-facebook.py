import json
import requests

token = 'EAAfxCMZChZCTYBAEhqwmo5kkMAtxAyCzXhhdKjCe4A3TYDZCaMzO79LwexKD6ZATmXkK8YX1cAgMDUpAKT2vj2WuTDnRZCxDavFfbxzfg9toTQc9t7HOKMYNRwL6IBJwV8uo1qZBm4ZBd1nHe4ZAjVXIKeiHx44WO4bEVnVZAfTbfmgZDZD'

graph = 'https://graph.facebook.com/v3.1/'
text = '10211847728938977?fields=events{start_time,end_time,name,description,place,type,ticket_uri}&access_token='+token


link = graph + text

yo = requests.get(link)
json_data = json.loads(yo.text)
print(json_data['events'])
