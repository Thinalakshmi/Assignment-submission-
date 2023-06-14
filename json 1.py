import json
with open("C://Users//muthuthillai.thina//downloads//words.json","r",encoding="utf-8")as word:
    data=word.read()
json_1=json.loads(data)#-->[{}{}{}]---:{"word":"home"}
dict_1={}
dic_final={}
for dic in json_1:
    key=dic["word"]#"home"#key
    value=dic["meanings"]
    for part in value:
        list=[]
        key_1=part["partOfSpeech"]#noun
        deff=part["definitions"]#
        for defi in deff:
                    
            list.append(defi["definition"])
            # print(list)
            dict_1[key_1]=list#value
        #print(dict_1)
    dic_final[key]=dict_1
    print(dic_final)
with open("C://Users//muthuthillai.thina//downloads//wor.json","w")as wor:
    wor.write(json.dumps(dic_final, indent=1))

        




