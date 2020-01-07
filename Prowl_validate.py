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

df_raw['Date'].values[1]

df1 = df_raw[df_raw.Date == '2017-01-23']

df1.groupby(['OnOffCam','Stop'])['Stop'].count()