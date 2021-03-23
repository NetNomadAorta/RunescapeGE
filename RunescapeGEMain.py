import requests
import numpy as np
from RunescapeGEInfo import map
from datetime import datetime

# function to convert unix-number to appropriate date format
def unixToDate(timeKey, iteration):
    unixLatest  = latest[map[list(responseLatest)[iteration]]['name']][timeKey] or 0
    latest[map[list(responseLatest)[iteration]]['name']][timeKey] \
        = datetime.utcfromtimestamp(unixLatest).strftime('%Y-%m-%d %H:%M:%S')

urlLatest = 'https://prices.runescape.wiki/api/v1/osrs/latest'

headers = {
    'User-Agent': 'Learning Python & GE Lookup',
    'From': 'snake82@hotmail.com'  # This is another valid field
}

while True:

    responseLatest = requests.get(urlLatest, headers=headers).json()['data']
    
    latest = {}
    
    # replace data's id to corresponding name and defines parameters for latest
    for i in range(len(list(responseLatest))-2): #delete the'-2'
        latest[map[list(responseLatest)[i]]['name']] = { \
            'high': responseLatest[list(responseLatest)[i]]['high'], \
            'low': responseLatest[list(responseLatest)[i]]['low'], \
            'highTime': responseLatest[list(responseLatest)[i]]['highTime'], \
            'lowTime': responseLatest[list(responseLatest)[i]]['lowTime'], \
            'margin': ( responseLatest[list(responseLatest)[i]].get('high',0) or 0 ) \
                - ( responseLatest[list(responseLatest)[i]].get('low',0) or 0 ), \
            'highAlch': map[list(responseLatest)[i]]['highalch'], \
            'alchProfit': ((map[list(responseLatest)[i]]['highalch'] or 0) \
                - ((responseLatest['561']['high'] or 0) \
                + (responseLatest[list(responseLatest)[i]]['high'] or 0))), \
            'id': list(responseLatest)[i] }
        
        # replace latest's unix timestamp to date (lowTime and highTime)
        unixToDate('highTime', i)
        unixToDate('lowTime', i)
    
    #type item names to search for market info
    item1 = 'Emerald bolts'
    item2 = 'Rune Javelin Heads'
    item3 = 'Abyssal bracelet(5)'
    item4 = 'Air Battlestaff'
    item5 = 'Onyx bolts (e)'
    item6 = 'Sapphire ring'
    item7 = 'Ring of recoil'
    
    # function to show key 'item' and it's keys and values
    def show(item):
        print()
        print('=== ' + item + ' ===')
        print(latest[item.lower()])
    
    # uses show function
    print('\n\n\n\n\n\n\n\n\n')
    # show(item1)
    show(item2)
    show(item3)
    show(item4)
    show(item5)
    show(item6)
    show(item7)
    
    print()
    lvl1Profit = latest['Ring of recoil'.lower()]['high'] \
        - ( latest['Sapphire ring'.lower()]['high'] \
        + latest['Cosmic rune'.lower()]['high'] \
        + + latest['Water rune'.lower()]['high'] )
    print('lvl-1 ring profit: ' + str(lvl1Profit))
    
    # name = 'mithril bolts'
    # show = np.array([ ['name', 'high', 'low','hightTime', 'lowTime', 'margin', 'id'],\
    #                 [latest[name], latest[name][ show[0][1] ]] ])
    # show = np.array([['name', 'high', 'low','hightTime', 'lowTime', 'margin', 'id'], \
    #                  ['mithril bolts', latest['mithril bolts']['high'], latest['mithril bolts']['low'], latest['mithril bolts']['highTime'], latest['mithril bolts']['lowTime'], latest['mithril bolts']['margin'], latest['mithril bolts']['id']]])
    
    # if input("Type x to exit: ") == 'x':
    #     break


# export to Excel (ONLY WORKS IF BREAK ACTIVATES OR WHILE LOOP STOPS FROM ABOVE)
import pandas as pd
df = pd.DataFrame(data=latest)
df = (df.T)
print (df)
df.to_excel('RunescapeGEMain.xlsx')
