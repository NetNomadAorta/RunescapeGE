import requests
from RunescapeGEInfo import map
from datetime import datetime

urlLatest = 'https://prices.runescape.wiki/api/v1/osrs/latest'

headers = {
    'User-Agent': 'Learning Python & GE Lookup',
    'From': 'snake82@hotmail.com'  # This is another valid field
}

while True:

    responseLatest = requests.get(urlLatest, headers=headers).json()['data']
    
    latest = {}
    
    # replace data's id to corresponding name and defines parameters for latest
    for i in range(len(list(responseLatest))):
        latest[map[list(responseLatest)[i]]['name']] = { \
            'id': list(responseLatest)[i], \
            'high': responseLatest[list(responseLatest)[i]]['high'], \
            'low': responseLatest[list(responseLatest)[i]]['low'], \
            'highTime': responseLatest[list(responseLatest)[i]]['highTime'], \
            'lowTime': responseLatest[list(responseLatest)[i]]['lowTime'], \
            'margin': ( responseLatest[list(responseLatest)[i]].get('high',0) or 0 ) \
                - ( responseLatest[list(responseLatest)[i]].get('low',0) or 0 ) }
        
        # replace latest's unix timestamp to date (lowTime and highTime)
        unixLatestHigh = latest[map[list(responseLatest)[i]]['name']]['highTime'] or 0
        latest[map[list(responseLatest)[i]]['name']]['highTime'] \
            = datetime.utcfromtimestamp(unixLatestHigh).strftime('%Y-%m-%d %H:%M:%S')
        unixLatestLow  = latest[map[list(responseLatest)[i]]['name']]['lowTime'] or 0
        latest[map[list(responseLatest)[i]]['name']]['lowTime'] \
            = datetime.utcfromtimestamp(unixLatestLow).strftime('%Y-%m-%d %H:%M:%S')

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('Mithril Bolts')
    print('===========================')
    print(latest['mithril bolts'])
    print()
    print('Rune Javelin Heads')
    print('===========================')
    print(latest['rune javelin heads'])
    print()
    print('Ruby Bracelet')
    print('===========================')
    print(latest['ruby bracelet'])
    
    # if input("Type x to exit: ") == 'x':
    #     break


# # export to Excel
# import pandas as pd
# df = pd.DataFrame(data=latest)
# df = (df.T)
# print (df)
# df.to_excel('RunescapeGEMain.xlsx')