import json

data = json.load(open("data.json"))


inr = input("Enter the Search word: ")

w = inr.lower()

if w in data:
	print (data[w])
else:
	print("check it!!")


