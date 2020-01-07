
import datetime
import pandas as pd
fname= '2017ProwlLineData.xlsx'
path = 'Data/'
outfile = '2017Prowl_condense.csv'

df_raw = pd.read_excel(path+ fname)
print (len(df_raw))

df1 = df_raw[(df_raw.Date == '2017-01-23' ) & (df_raw.Route == 'Peak Prowl Line')]
df1.groupby('Stop')['Stop'].count()
### 263382
# # df_raw.head(10)
# # df_raw.columns
# df_raw['Unhashed card ID']
'''
['Id', 'Date', 'Time', 'Bus', 'Driver', 'Route', 'Stop', 'Count',
Device', 'Passenger type', 'On/Off', 'Lat', 'Lng', 'Speed',
'Hashed card ID', 'Unhashed card ID']
'''

#step1: drop none value in rows
df_raw['Unhashed card ID'].dropna()
df_raw1 =df_raw.dropna()
print (len(df_raw1))
# 204384/263382
### 204384
# summarize information
Stud_ID = df_raw1['Unhashed card ID'].unique()
len(Stud_ID)


#step2: slect useful columns
df_condense = df_raw1[['Date','Time','Stop','Unhashed card ID']]

#step3: add extra informations
on_campus = ['Cunningham Hall (Cunn)',
            'UWM Golda Meir Library (Lib)' ,
            'Sandburg Residence Hall (Sand)' ,
            'UWM Union (Union)',
            'Non-Peak Hours UWM KIRC (KIRC-S)'
            ]
off_campus =['Cambridge Commons (CC-S)',
            'Cambridge Commons - Northbound (CC-N)',
            'Capitol and Humboldt Park and Ride (C/H)',
            'Kenilworth Square Apartments (KNW)',
            'RiverView Residence Hall (RVW)'
            ]

def f(row):
    if row['Stop'] in on_campus:
        val = 0
    elif row['Stop'] in off_campus:
        val = 1
    else:
        val = -1
    return val

df_condense['OnOffCam'] = df_condense.apply(f, axis=1)
df_condense['Weekday'] = df_condense['Date'].dt.weekday_name

# df_condense.groupby(['OnOffCam','Stop']).count()

df_condense.to_csv(path+ outfile,index=False)