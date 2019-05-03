

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
df_person.groupby(['OnOffCam'])['Date'].count()

def OO_count(stud = 280,df_raw= df_raw):
    df_person = df_raw[df_raw.index == Stud_ID[stud] ]
    ser = df_person.groupby(['OnOffCam'])['Date'].count()
    return ser


OnOff_ser = OO_count(stud = 7569)

OnOff_ser[0]+OnOff_ser[1] >0

count = 0
for i in range(0,len(Stud_ID)-1 ):
    OnOff_ser = OO_count(stud = i)
    try:
        num = OnOff_ser[0] + OnOff_ser[1]
    except KeyError:
        print (i)
    if num > 10:
        count +=  1
    
print (count)


# OD Infering---- On-off Campus
df_OD =df_person.groupby(['OnOffCam','Stop']).count()
# df_person.groupby(['OnOffCam','Stop']).size()
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



