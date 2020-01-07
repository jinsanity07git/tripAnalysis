

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

stud = 956
df_person = df_raw[df_raw.index == Stud_ID[stud] ]
# df_person.groupby(['OnOffCam','Stop','Date']).count()

# weekdays categorization
# #####df_person.groupby(['Weekday','OnOffCam','Stop'])['Date'].count()
df_person.groupby(['Weekday','Stop','OnOffCam'])['Date'].count()

# subtotal---- On Campus count summation
df_person.groupby(['OnOffCam'])['Date'].count()

# OD Infering---- On-off Campus
df_person.groupby(['OnOffCam','Stop'])['Date'].count()


df_person.count()[1]

###01 analyze students' count profile
travel_count = []
StuID =     []
for stud in range(0,len(Stud_ID)):
    # print(stud)
    df_person = df_raw[df_raw.index == Stud_ID[stud] ]
    num = df_person.count()[1]
    travel_count.append(num)
    StuID.append(stud)

s = pd.Series(travel_count)
print ( s.describe() )
s.hist( bins=40)

df = pd.DataFrame(list(zip(StuID, travel_count)), columns =['ID','Cnt']) 

print (  s.quantile( q=0.64) * len(Stud_ID))
print (  0.64 * len(Stud_ID))

df[df.Cnt >60 ].count()


###02 analyze  count CDF
c1 = []
c2 = []
c3 = []
SumP ,intV = 0,5
for trips in range(0,230,intV):
    # print(stud)
    c1.append(trips) 
    Sum = df[df.Cnt < trips+intV ].count()[0]
    c3.append(Sum)
    num = Sum - SumP
    SumP =  Sum
    c2.append(num)

df2 = pd.DataFrame(list(zip(c1, c2,c3)), columns =['Trips','StudentsNum','ACC']) 
df2['CDF'] = round(df2['ACC']/len(Stud_ID),2)