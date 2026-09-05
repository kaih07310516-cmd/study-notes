import json
data = '''{
    "name" : "hk",
    "phone" : {
        "type" : "intl",
        "number" : " +15060258626"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

input = '''[
    {   "id" : "001",
        "x"  : "2",
        "name" : "hk"
    },
    {   "id" : "009",
        "x"  : "7",
        "name" : "hyx"
    }
]'''

info = json.loads(input)
print("User count",len(info))
for item in info:
    print('Name:',item["name"])
    print('id:',item["id"])
    print('Attribute',item["x"])