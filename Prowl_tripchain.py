

import pandas as pd
fname= '2017ProwlLineData.xlsx'
path = 'Data/'
df_raw = pd.read_excel(path+ fname)

df_raw.head(50)

df_raw.columns
df_raw['Unhashed card ID']


df_person = df_raw[df_raw['Unhashed card ID'] == 100592 ]

df_person[['Date','Time','Stop','Bus']]

