import requests
import json

# r=requests.get("https://images.bayut.com/thumbnails/173137475-800x600.jpeg")

# with open("comic.png","wb")as f:
#      f.write(r.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)

#get 
# payload={"page":2,"count":25}
# r=requests.get("https://httpbin.org/get",params=payload)
# print(r.text)
# print(r.url) 

#put
# payload={"username":"sdfsdf","password":"sdfkfd"}
# r=requests.post("https://httpbin.org/post",data=payload)
# print(r.text)
# dic=r.json()
# print(dic["form"])

##basic auth
# r=requests.get("https://httpbin.org/basic-auth/renin/qwerty",auth=('renin','qwerty'))
# print(r.text)

##timeout 
# r=requests.get("https://httpbin.org/basic-auth/renin/qwerty",timeout=3)
# print(r)

##delay
r=requests.get("https://httpbin.org/delay/6",timeout=3)
print(r)