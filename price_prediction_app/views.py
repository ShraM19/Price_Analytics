from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def predict_price(request):
    if request.method == 'POST':
        # Extract data from the POST request
        data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from the request body
        product_name = data.get('productName')
        date = data.get('date')

        # Make the API call to get the predicted price
        url = "https://price-analytics.p.rapidapi.com/search-by-term"
        payload = {
            "source": "amazon",
            "country": "in",
            "values": product_name  # Use the received product_name in the payload
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "1ac19f1354msh88e15b12358b62cp1f3cc9jsn1a6dbf3bb9f4",
            "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
        }
        response = requests.post(url, data=payload, headers=headers)

        # Extract the predicted price from the response JSON
        predicted_price = response.json().get('predicted_price', 'Price not available')

        # Return the predicted price as JSON response
        return JsonResponse({'predicted_price': predicted_price})

    # Render the index.html template if it's not a POST request
    return render(request, 'index.html')