import requests
import pyfiglet
from termcolor import colored as cld
import random

print(cld(pyfiglet.figlet_format("DAD 2000"), color= "red"))


url = "https://icanhazdadjoke.com/search?"

inp = input("What joke do you prefer:")
print("\n ")

requ = requests.get(url,

	headers = {"Accept" : "application/json"},
	params =  {"term" : inp}  
)

outs = requ.json()

resu = len(outs["results"])

if resu != 0:

	print (f"There are totally {resu} {inp} jokes available!!!! \n")

	inp_select = input("How do you prefer,'all' or 'random' joke: ").lower()
	print("\n")

	if inp_select == "all":

		for jk in range(resu):

			kim = outs["results"][jk]["joke"]
			
			print(jk+1,".",kim,"\n")

	elif inp_select == "random":

		print(outs["results"][random.randint(0, resu-1)]["joke"])

	else:
		print("check the input!!")

else:
	print(f"Sorry, :( There is no jokes available in {inp} type")

