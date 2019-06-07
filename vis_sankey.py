from pyecharts.charts import Page, Sankey
from pyecharts import options as opts
import pandas as pd
import json
import sys


def Cnode_link(ls,arr):
    """
    将node list 转换为 list of {name : node}   
    将link array 转换为 list of {'source':arr[i][0],'target':arr[i][1],'value': int(arr[i][2])} 
    return A tuple
    """
    k_lst, v_lst = [], []
    i=0
#     k_dict= {}
    if isinstance(ls, list):
        for s in ls:
            k_dict = {'name': s} 
            k_lst.append(k_dict)
        for row in arr:
            v_dict = {'source':arr[i][0],'target':arr[i][1],'value': int(arr[i][2])}   ##intger in value
            v_lst.append(v_dict)
            i += 1
    return k_lst, v_lst

# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))
	
	
# ### 1.read data from  file

'''
python main.1.py '{"basic_config": {"width": "800", "height": "600", "title_top": ["0"], "color_b": "#ffffff", "title_pos": ["1"], "title_color": "#000000", "title": "桑基图", "subtitle": "样例", "f_size_m": "18", "f_size_s": "12", "sub_color": "#ff2600"}}' sankeychart.xlsx out.html
'''

# config_data=json.loads( '{"basic_config": {"width": "800", "height": "600", "title_top": ["0"], "color_b": "#ffffff", "title_pos": ["1"], "title_color": "#000000", "title": "桑基图", "subtitle": "样例", "f_size_m": "18", "f_size_s": "12", "sub_color": "#ff2600"}}')
# inputdata = 'Data/sankeychart_Boss.xlsx'
inputdata = 'Data/sankeychart_Prowl.xlsx'

outdata = 'notebook/out.html'

print("break ponit 2")

# CNG =config_data['basic_config']


df1=pd.read_excel(inputdata)

print("break ponit 4")

### 1.图形初始化  参数
# for k in CNG:
#     exec(k + " = CNG[k]")  
    ### pass value to a variable name (key as the variable)

### 2-3 节点 和 节点关系
list_node_value = df1['1.节点'][2:].dropna()
list_link_source = df1[['2. 节点关系','2.B','2.C']][2:].dropna()
ls1 = list_node_value.tolist()
array1 =list_link_source.as_matrix()

print("break ponit 5")
### use Cnode_link to do 
tuple_nl =Cnode_link(ls1,array1)
nodes = tuple_nl[0]
links = tuple_nl[1]
	

print("break ponit 3")


# ### 3.generate sankey char   t with basic input
sankey = Sankey()  


print("break ponit 3.1")
sankey.add("sankey", nodes, links, linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source")
             , 
              ) 


print("break ponit 3.2")

sankey.render(outdata)

print("break ponit 1")
print("1")

