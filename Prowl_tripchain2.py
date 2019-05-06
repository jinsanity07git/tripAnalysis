

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

def student_max(stud = 1, df_raw= df_raw ):
    df_person = df_raw[df_raw.index == Stud_ID[stud] ]
    df_ser = df_person.groupby(['OnOffCam','Stop'])['Stop'].size()
    max_0,max_1 = 0,0
    for i,n in enumerate(df_ser):
        index_tup = df_ser.index[i]
        # print (index_tup[1] ,n) 

        if 0 in index_tup:
            if df_ser[index_tup] > max_0:
                max_0 = df_ser[index_tup]
                inx_stop0 =  index_tup[1]
        else:
            if df_ser[index_tup] > max_1:
                max_1 = df_ser[index_tup]
                inx_stop1 =  index_tup[1]
    return  (Stud_ID[stud], inx_stop0,max_0,inx_stop1,max_1)
    # print (i,n)


student_max(stud = 2322)[2]

# tup = student_max(stud = i)

# '{},{},{},{},{}'.format(100968,'UWM Golda Meir Library (Lib)',29,'RiverView Residence Hall (RVW)',32)

outfile = 'Data/tripchain_df1.csv'
with open(outfile,'w') as file:
    file.write('ID,Stop_0,Cnt_0,Stop_1,Cnt_1 \n')
    for i in range(0,len(Stud_ID)-1):
        tup = student_max(stud = i)
        file.write('{},{},{},{},{} \n'.format(tup[0],tup[1],tup[2],tup[3],tup[4]))