import json
with open("C://Users//muthuthillai.thina//Desktop//Python//sample_data.json","r")as data:
    read_data=data.read()
data_convert=json.loads(read_data)
access_parameterList=data_convert["parametersList"]
#print(access_parameterList)
list_1=[]
for dic in access_parameterList:
    dict_1={}
    value_1=dic["parameterName"]
    #print(value_1)#BOD
    value_2=dic["min"]
   # print(value_2)
    value_3=dic["max"]
    #print(value_3)
    value_4=dic["avg"]
    #print(value_4)
    
    dict_1['parameterName']=value_1
    dict_1['min_value']=value_2
    dict_1['max_value']=value_3
    dict_1['avg_value']=value_4
    #print(dict_1)
    #print(dict_1)
#list_1=[]
    list_1.append(dict_1)
print(list_1)
with open("C://Users//muthuthillai.thina//Desktop//Python//task.json","w")as task:
    task.write(json.dumps(list_1, indent=1))
   
       


