import WazeRouteCalculator
import pandas as pd
import timeit
import json


start = timeit.default_timer()
# https://github.com/kovacsbalu/WazeRouteCalculator

input01   = 'inprocess_results/points_NB.csv'
output01  = 'inprocess_results/ODlist_NB.csv'
output02  = 'inprocess_results/ODlMtx_NB.csv'
df = pd.read_csv(input01)

Num  = len(df)
list_set = []
for i in range(Num):
    for j in range(Num):
        if {i,j} not in list_set:
            list_set.append({i,j})


len(list_set)

list_set = []
for i in range(Num):
    for j in range(i+1 ,Num):
        list_set.append((i,j))

t_delta = 10
dict_i = {}
for i in range(len(list_set)):
    A,B = list_set[i]
    from_address ='{},{}'.format( df.loc[A,'lat'],df.loc[A,'lon'] )
    to_address = '{},{}'.format( df.loc[B,'lat'],df.loc[B,'lon'])
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, 'US')
    try: 
        route_time, route_distance = route.calc_route_info(time_delta=t_delta)
    
    except:
        route_time, route_distance = None,None
    dict_i.update({list_set[i] : route_distance} )


## refilled None valuse
dist_list = [i for i in  dict_i.values()]
index_list = [ k for k,v in  dict_i.items() if v == None]
count  = 1

while None in dist_list: 
    print ('round: {}'.format(count))

    for i in  range(len(index_list)):
        row,col = index_list[i]
        from_address = '{},{}'.format( df.loc[row,'lat'],df.loc[row,'lon'])
        to_address = '{},{}'.format( df.loc[col,'lat'],df.loc[col,'lon'])
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, 'US')
        try: 
            route_time, route_distance = route.calc_route_info(time_delta=t_delta)
        
        except:
            route_time, route_distance = None,None
        dict_i.update({list_set[i] : route_distance} )
        print ('Blank in  {} has been filled '.format(list_set[i]))
    dist_list = [i for i in  dict_i.values()]
    index_list = [ k for k,v in  dict_i.items() if v == None]

    count += 1
        
print (dict_i)

with open(output01 ,'w') as outfile:
    for k,v in  dict_i.items() :
        outfile.write ('{},{},{} \n'.format(k[0],k[1],v))


#2nd part concert a distance dict to an OD Matrix
import numpy as np

## create a np array matrix to build a dataframe
array = np.array([[0,]*4]*4)
df = pd.DataFrame(array)

for k,v in dict_i.items():
    row,col = k
    df.loc[row,col] = v
    df.loc[col,row] = v

df.to_csv(output02)





stop = timeit.default_timer()
print('Time: ', stop - start)  

# df_out.to_csv(output01)