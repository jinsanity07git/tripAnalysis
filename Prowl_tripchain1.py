

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
df_person.groupby(['OnOffCam','Stop']).size()

df_OD.plot('barh')
df_OD.columns

df_tem =  df_OD[df_OD['Date'] > 15]
df_tem.names

df_OD.to_json()

len(df_OD)
df_OD[[5]]

df_OD[(0, 'Cunningham Hall (Cunn)')]

df_OD.index[5]