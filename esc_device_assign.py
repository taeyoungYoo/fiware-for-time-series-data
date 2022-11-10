import requests

custom_device_id = 'acoustic02'

headers = {
    'fiware-service': 'youngcustomdevice',
    'fiware-servicepath': '/escTest',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'devices': [
        {
            'device_id': custom_device_id,
            'entity_name': 'urn:ngsi-ld:Device:'+custom_device_id,
            'entity_type': 'Device',
            'timezone': 'Asia/Seoul',
            'attributes': [
                {
                    'object_id': 't',
                    'name': 'acoustic',
                    'type': 'Property',
                    'metadata': {
                        'unitCode': {
                            'type': 'Property',
                            'value': 'PER',
                        },
                    },
                },
            ],
            'static_attributes': [
                {
                    'name': 'category',
                    'type': 'Property',
                    'value': [
                        'sensor',
                    ],
                },
                {
                    'name': 'supportedProtocol',
                    'type': 'Property',
                    'value': [
                        'ul20',
                    ],
                },
            ],
        },
    ],
}

response = requests.post('http://172.16.63.191:4041/iot/devices', headers=headers, json=json_data)