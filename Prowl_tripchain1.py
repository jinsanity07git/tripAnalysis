

import pandas as pd
fname= '2017Prowl_condense.csv'
path = 'Data/'
df_raw = pd.read_csv(path+ fname,index_col='Unhashed card ID')
df_raw.head(10)
df_raw.columns
"""
Index(['Date', 'Time', 'Stop', 'OnOffCam'], dtype='object')
"""



Stud_ID = df_raw.index.unique()
len(Stud_ID)  #7572

stud = 8
df_person = df_raw[df_raw.index == Stud_ID[stud] ]
# df_person.groupby(['OnOffCam','Stop','Date']).count()

# weekdays categorization
# #####df_person.groupby(['Weekday','OnOffCam','Stop'])['Date'].count()
df_person.groupby(['Weekday','Stop','OnOffCam'])['Date'].count()

# subtotal---- On Campus count summation
df_person.groupby(['OnOffCam'])['Date'].count()

# OD Infering---- On-off Campus
df_OD =df_person.groupby(['OnOffCam','Stop']).count()
df_ODp=df_person.groupby(['OnOffCam','Stop']).size()

'''
type(df_ODp) # pandas.core.series.Series
type(df_OD)

Only series can be multi indexed????
dataframe need to use loc
'''
df_ODp[0,'Non-Peak Hours UWM KIRC (KIRC-S)']
df_OD.xs(0)
df_OD.loc[0,('Cunningham Hall (Cunn)')]
for i,n in enumerate(df_OD.loc[0,]['Date']):
    print (i,n)
df_OD.loc[0,]['Date'] 

df_tem =  df_ODp[df_ODp['Date'] > 15]
df_tem[0]
df_OD.to_json()
len(df_OD)

df_OD.index[1]

df_OD[0]
df_OD.index

df_OD[5:]
df_OD[0, 'Capitol and Humboldt Park and Ride (C/H)']

df_person.index
df_person['100968']

