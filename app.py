# price_prediction_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def predict_price(request):
    if request.method == 'POST':
        product_name = request.POST.get('productName')
        date = request.POST.get('date')

        # Print received data
        print("Received Product Name:", product_name)
        print("Received Date:", date)

        # Make the API call to get the predicted price
        url = "https://price-analytics.p.rapidapi.com/search-by-term"
        payload = {
            "source": "amazon",
            "country": "in",
            "values": product_name
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "1ac19f1354msh88e15b12358b62cp1f3cc9jsn1a6dbf3bb9f4",
            "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
        }
        response = requests.post(url, data=payload, headers=headers)
        predicted_price = response.json().get('predicted_price', 'Price not available')

        # Return response to frontend
        return JsonResponse({'message': 'Got it'})

    return render(request, 'index.html')