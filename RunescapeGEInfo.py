import requests

urlMapping = 'https://prices.runescape.wiki/api/v1/osrs/mapping'

headers = {
    'User-Agent': 'Learning Python & GE Lookup',
    'From': 'snake82@hotmail.com'  # This is another valid field
}

mapping = requests.get(urlMapping, headers=headers).json()

map = {}

for i in range(len(mapping)):
    map[str(mapping[i]['id'])] = { 'name': mapping[i].get('name').lower(), 'highalch': \
       mapping[i].get('highalch'), 'members': mapping[i].get('members'), \
       'limit': mapping[i].get('limit') }
