import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

data = response.json()

#print(data["title"])

#https://api.example.com/search?q=python


# url = "https://api.example.com/search"

# params = {
# 	"q":"python"
# }

# response = requests.get(url,params=params)

#print(response.text)

#post api

data = {
	"name": "ramesh",
	"age":25
}

url = "https://httpbin.org/post"

response = requests.post(

     url, 
     json=data
 
	)

print(response.text)



