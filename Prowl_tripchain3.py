

import pandas as pd
fname= 'tripchain_df1.csv'
path = 'Data/'
df_raw = pd.read_csv(path+ fname,index_col='ID')
df_raw.head(10)
df_raw.columns
len(df_raw)   # 3084
"""
Index(['Stop_0', 'Cnt_0', 'Stop_1', 'Cnt_1 '], dtype='object')
"""

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



df_raw[df_raw['Stop_0']==on_campus[0]  ]

df_sub = df_raw.loc[ (df_raw['Stop_0']==on_campus[3]) & (df_raw['Stop_1']==off_campus[3] )  ]


sum(df_sub['Cnt_0'])
sum(df_sub['Cnt_1 '])




outfile = 'Data/tripchain_df2.csv'
with open(outfile,'w') as file:
    file.write('Stop_0,Stop_1,Cnt_0,Cnt_1,Ave\n')
    for i in range(0,len(on_campus)):
        for j in range(0,len(off_campus)):
            Stop_0,Stop_1= on_campus[i],off_campus[j]
            df_sub = df_raw.loc[ (df_raw['Stop_0']== Stop_0) & (df_raw['Stop_1']==Stop_1)]
            Cnt_0 = sum(df_sub['Cnt_0'])
            Cnt_1 = sum(df_sub['Cnt_1 '])
            Ave = (Cnt_0+ Cnt_1)*0.5

            file.write('{},{},{},{},{} \n'.format(Stop_0,Stop_1,Cnt_0,Cnt_1,Ave))