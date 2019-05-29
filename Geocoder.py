import requests
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderQueryError

import pandas as pd
import csv
import time

start = time.time()
print("hello")


with open('../Google_API.txt' ) as file:
    myKey  = file.read()


def geo_coder(my_address= "Union South UWM" ):
    loc = None
    geolocator = GoogleV3(api_key=myKey, timeout=3)
    try:
        loc = geolocator.geocode(my_address)
        # print(location.latitude, location.longitude)
    except GeocoderTimedOut:
        print("Error: geocode failed on input %s with message "%(my_address))
        loc = my_address
    except GeocoderQueryError :
        print ('GeocoderQueryError; %s'%(my_address) )
        loc = my_address
    return loc

# print(location.address)
# print (location.latitude,location.longitude)


path  = 'Data/2019_02.csv'

df = pd.read_csv(path,encoding = 'unicode_escape')
df.columns

'''
Index(['Requested Pick Up Time', '# of Pass-engers', 'Pick Up Location',
       'Drop Off Location', 'Cancellation Time', 'Pickup Time',
       'Drop Off Time', 'Wait Time (min)', 'Passenger Canceled?',
       'Cancellation Message', 'lat', 'long'],
      dtype='object')
'''
# index = 50
# print (df['Pick Up Location'][index])
# print (len(df['Pick Up Location'][index]))

df['lat'],df['long']  = None,None


num = len(df)
add_set = set()
len_set = set()

for i in range(num):
    address = df['Pick Up Location'][i]
    if len(address) > 40:
        location =geo_coder(address)
        if type(location) != type('string') and type(location) != type(None) :
            df['lat'][i] = location.latitude
            df['long'][i] = location.longitude
        else:
            df['lat'][i] = location
            add_set.add(location)
            end = time.time()
            print(end - start)
    else:
        df['long'][i] = address
        add_set.add(address)
        print ('iter:' + str(i))


# df['lat'][3500:4000] 
# df['lat'][200] 
# df['long'][200] 
# type(df['lat'][2])


df.to_csv('boss02_Origin.csv')


with open('outliers.csv','w') as csvfile:
        # wr = csv.writer(csvfile)
        for line in add_set:
            try:
                csvfile.write(line + ',\n')
            except:
                pass

        for line in len_set:
            try:
                csvfile.write(line + ',\n')
            except:
                pass


# with open(path,'rw') as file: 
#     for line in file:
#         if 'Requested Pick Up' in line:
#             print  (line)

# import re 
# path  = 'Data/2019_02'
# with open(path+ '.csv', encoding="utf8", errors='ignore') as f_in:
#     with open(path+ '_new.csv', 'w') as f_out:
#         # file = f_in.read()
#         for line in f_in.readlines():
#             if 'Requested Pick Up' in line:
#                 old = line.rstrip('\n')
#                 new =  old +', Origin' + ',Destination'
#             else:

        
#         f_out.write(new)