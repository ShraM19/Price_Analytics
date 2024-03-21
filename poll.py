import requests

url = "https://price-analytics.p.rapidapi.com/poll-job/65e73a3d24574e380022eb4c"

headers = {
	"X-RapidAPI-Key": "1ac19f1354msh88e15b12358b62cp1f3cc9jsn1a6dbf3bb9f4",
	"X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())