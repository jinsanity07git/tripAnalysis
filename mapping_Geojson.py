
import json
import pandas as  pd
from geojson import Point, Feature, FeatureCollection, dump
import numpy as np
import  math 

Rela_ad = 'inprocess_results/'
# input01  = 'inprocess_results/centers.json'
# input02  = Rela_ad + '02_ODflow.csv'


# # outfile01 = Rela_ad + 'flow.geojson'
# df =pd.read_csv(input02,header=None ) 


input01  = 'inprocess_results/center_prowl.json'
input02  = Rela_ad + 'tripchain_df2.csv'


outfile01 = Rela_ad + 'flow_prowl.geojson'
df =pd.read_csv(input02,header=None ) 
df = df.drop([0], axis=0)
## ralabel index from start with 1  to start  witrh 0 

df.index = range(len(df))
with open(input01,'r') as file:
    dic = json.load(file)




### prepare a color dictionary for each cluster 

from palettable.colorbrewer.qualitative import Paired_10
# df[1] + df[0]
series = pd.concat([df[1] ,df[0]])
array01 = series.unique() 
# array01.np.append( append)
dic_color = {}
for i in range(len(array01)):
    dic_color.update( {array01[i] : Paired_10.hex_colors[i]} )


dic_fCol = {
  "type": "FeatureCollection",
  "features": []
  }

# dic_feat = {"type": "Feature",
#       "properties": {
#         "stroke": "#555555",
#         "stroke-width": 4,
#         "stroke-opacity": 1
#       },
#       "geometry": {
#         "type": "LineString",
#         "coordinates": [
#           [
#             -87.92547225952148,
#             43.084310566406344
#           ],
#           [
#             -87.89937973022461,
#             43.088573092465595
#           ]
#         ]
#       }
#     }

# df.iloc[0,2]
df[1]
ls_feat = []
df[2] = df[2].astype(float)
max_flow = max(df[2])
for index in range(len(df)):

    dic_feat = {"type": "Feature",
        "properties": {
            "stroke": "#555555",
            "stroke-width": 4,
            "stroke-opacity": 0.4,
            'direction':    '0->1',
            'flow'      :  100
        },
        "geometry": {
            "type": "LineString",
            "coordinates": []
            }
        }
    # index = i
    # max_flow =  max(df[2])
    A,B = df[0][index] , df[1][index]
    cood_ls = [dic[A],dic[B]]
    dic_cood = {"coordinates":cood_ls}
    dic_feat["geometry"].update(dic_cood)
    ls_feat.append(dic_feat)
    dic_direct = {'direction': A + '->' +B }
    dic_feat['properties'].update(dic_direct)
    ## flow index
    flow = df[2][index]
    numerator  = flow
    # if flow == 0: 
    #     numerator = 0 
    # else:
    #     numerator =  math.log(flow)
    width = numerator/max_flow *20
    dic_feat['properties'].update({"stroke-width":int(width)})
    dic_feat['properties'].update({"flow":int(flow)})
    dic_feat['properties'].update({"stroke":dic_color[A]})
# math.log(max_flow,1.01)
# math.log(51)/math.log(10000)
# base = 1.01

# math.log(10,base)
# math.log(max_flow,base)
dic_fCol.update({'features' : ls_feat})

with open(outfile01, 'w') as f:
   dump(dic_fCol, f)
