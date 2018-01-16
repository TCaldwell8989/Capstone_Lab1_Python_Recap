import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

base_url = 'https://api.fixer.io/latest?base=USD'
data = requests.get(base_url).json()
cad = data["rates"]["CAD"]
print("The latest exchange rate is 1 USD to " +str(cad)+ " CAD\n")

pp.pprint(data)