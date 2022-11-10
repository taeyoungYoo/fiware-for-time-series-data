import requests

headers = {
    'Content-Type': 'text/plain',
}

params = {
    'k': 'rtestaeyoungtest0710',
    'i': 'acoustic02',
}

# 실제 데이터를 측정하는 코드가 들어가는 부분
acquired_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
sending_data = ''
for i in range(len(acquired_data)):
    sending_data += 'c'+str(i+1)+'|'+str(acquired_data[i])+'|'
sending_data = sending_data[:-1]

response = requests.post('http://172.16.63.191:7896/iot/d', params=params, headers=headers, data=sending_data)