import ruamel.yaml as yaml
import json
if __name__ == '__main__':
    print("lam viec voi file yaml")
    with open ("user.yaml","r") as stream :
        user_yaml= yaml.safe_load(stream)
    print("Print Type of user_yaml")
    print(type(user_yaml))
    print("-----------------")
    for key in user_yaml:
        print(key)
    print("-----------------")  
    print("print value of key'id'")
    print(user_yaml["id"])
    print("-----------------") 
    print("print value of key 'first_name'")
    print(user_yaml["first_name"])
    print("-----------------") 
    print("print value of key 'last_name'")
    print(user_yaml["last_name"])
    print("-----------------") 
    print("print value of key 'birth_date'")
    print(user_yaml["birth_date"])
    print("-----------------") 
    print("print value of key 'address'")
    print(user_yaml["address"])
    adr=user_yaml["address"][1]
    user_json= json.dumps(user_yaml,default=str, indent=4)
    print("Structure json")
    print(user_json)
    file=open("user.json","w")
    file.write(user_json)
    file.close