
import json
import pandas as  pd
from geojson import Point, Feature, FeatureCollection, dump

Rela_ad = 'inprocess_results/'
input01  = 'inprocess_results/centers.json'
input02  = Rela_ad + '02_ODflow.csv'


outfile01 = Rela_ad + 'flow.geojson'

with open(input01,'r') as file:
    dic = json.load(file)

df =pd.read_csv(input02,header=None) 

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

ls_feat = []
max(df[2])
for index in range(len(df)):

    dic_feat = {"type": "Feature",
        "properties": {
            "stroke": "#555555",
            "stroke-width": 4,
            "stroke-opacity": 1,
            'direction':    '0->1',
            'flow'      :  100
        },
        "geometry": {
            "type": "LineString",
            "coordinates": []
            }
        }
    # index = i
    max_flow =  max(df[2])
    A,B = df[0][index] , df[1][index]
    cood_ls = [dic[A],dic[B]]
    dic_cood = {"coordinates":cood_ls}
    dic_feat["geometry"].update(dic_cood)
    ls_feat.append(dic_feat)
    dic_direct = {'direction': A + '->' +B }
    dic_feat['properties'].update(dic_direct)
    ## flow index
    flow = df[2][index]
    width = flow/max_flow * 20
    dic_feat['properties'].update({"stroke-width":int(width)})
    dic_feat['properties'].update({"flow":int(flow)})
    

dic_fCol.update({'features' : ls_feat})

with open(outfile01, 'w') as f:
   dump(dic_fCol, f)
