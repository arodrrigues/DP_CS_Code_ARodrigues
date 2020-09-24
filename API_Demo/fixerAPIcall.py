import requests
import json

#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()

# tool to read the contencts of a fil einto a list

resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)

#Converts response to JSON
data = resp.json()

print(data["base"])
print(data["rates"]["USD"])

#print(data)
