

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

# OnOff_ser[0]+OnOff_ser[1] >0

# df_filter[df_filter.index == '100968']
mintrip_std = 5
count = 0
df_filter = df_raw

outfile = 'Data/filter_df1.csv'

for i in range(0,len(Stud_ID)-1 ):
    OnOff_ser = OO_count(stud = i)
    try:
        num = OnOff_ser[0] + OnOff_ser[1]
        filterIn = True
    except KeyError:
        print (i)
        filterIn = False
        num = 0
        df_filter = df_filter.drop(Stud_ID[i])
    if filterIn :     
        if num <= mintrip_std:
            try:
                df_filter = df_filter.drop(Stud_ID[i])
            except KeyError:
                print ("key: " + Stud_ID[i])
        else :

            count += 1


print (count)

outfile = 'Data/filter_df1.csv'
df_filter.to_csv(outfile)


len(df_filter)
len(df_raw)



