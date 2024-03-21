import requests

url = "https://product-price-history.p.rapidapi.com/price-history"

querystring = {"country_iso2":"in","gtin":"194253401179","last_x_months":"1"}

headers = {
	"X-RapidAPI-Key": "1ac19f1354msh88e15b12358b62cp1f3cc9jsn1a6dbf3bb9f4",
	"X-RapidAPI-Host": "product-price-history.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())