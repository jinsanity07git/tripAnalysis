import WazeRouteCalculator
import pandas as pd
import timeit


start = timeit.default_timer()
# https://github.com/kovacsbalu/WazeRouteCalculator

input01   = 'inprocess_results/points_NB.csv'
output01  = 'inprocess_results/ODMatrix_NB.csv'
df = pd.read_csv(input01)

# df.loc[2,'lat']
# # from_address = 'Budapest, Hungary'
# from_address = '43.09390083293419,-87.9035854339599s6'
# to_address = '43.09390083293419,-87.90358543395996'
# region = 'US'
# route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
# route_time, route_distance = route.calc_route_info()

t_delta = 10
Num  = len(df)
dict_i = {}
for i in range(Num):
    from_address ='{},{}'.format( df.loc[i,'lat'],df.loc[i,'lon'] )
    dict_j = {}
    for j in range(Num):
        to_address = '{},{}'.format( df.loc[j,'lat'],df.loc[j,'lon'])
        
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, 'US')
        try: 
            route_time, route_distance = route.calc_route_info(time_delta=t_delta)
        
        except:
            route_time, route_distance = None,None
        dict_j.update({j : route_distance})
    dict_i.update({i : dict_j})

df_out =pd.DataFrame.from_dict(dict_i, orient='index')



import numpy as np
# find col, index where Nan value exists?
count = 1
while pd.isnull(df_out).any(1).any() == True:
    idx,idy= np.where(pd.isnull(df_out))
    num = len(idx)
    print ('round {}'.format(count))

    for i in range(num):
        row,col = idx[i],idy[i]
        from_address = '{},{}'.format( df.loc[row,'lat'],df.loc[row,'lon'])
        to_address = '{},{}'.format( df.loc[col,'lat'],df.loc[col,'lon'])
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, 'US')
        try: 
            route_time, route_distance = route.calc_route_info(time_delta=t_delta)
        
        except:
            route_time, route_distance = None,None
        df_out.loc[row,col] = route_distance
        print ('Blank in row {}, col {} has been fixed'.format(row, col) )


    count += 1


stop = timeit.default_timer()

print('Time: ', stop - start)  

df_out.to_csv(output01)