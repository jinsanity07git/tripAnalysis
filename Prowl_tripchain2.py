

import pandas as pd
fname= 'filter_df1.csv'
path = 'Data/'
df_raw = pd.read_csv(path+ fname,index_col='Unhashed card ID')
df_raw.head(10)
# df_raw.columns
len(df_raw)   # 198279
"""
Index(['Date', 'Time', 'Stop', 'OnOffCam'], dtype='object')
"""

Stud_ID = df_raw.index.unique()
len(Stud_ID)  #7572   3085

stud = 8
df_person = df_raw[df_raw.index == Stud_ID[stud] ]

df_ser = df_person.groupby(['OnOffCam','Stop'])['Stop'].size()


df_ser[0,'Non-Peak Hours UWM KIRC (KIRC-S)']
type(df_ser[0,])


for i,n in enumerate(df_ser):
    index_tup = df_ser.index[i]
    print (index_tup[1] ,n) 
    max_0 = 0
    max_1 = 0
    if 0 in index_tup:
        if df_ser[index_tup] > max_0:
            max_0 = df_ser[index_tup]
            inx_stop0 =  index_tup[1]
    else:
        if df_ser[index_tup] > max_1:
            max_1 = df_ser[index_tup]
            inx_stop1 =  index_tup[1]

    # print (i,n)