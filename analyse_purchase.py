from collections import defaultdict
import json

def analyze_purchase_data(json_data):
    # Parse JSON data
    data = json.loads(json_data)
    
    # Group data by month
    monthly_data = defaultdict(list)
    for date_str, info in data.items():
        month = date_str[:7]
        monthly_data[month].append(info)
    
    # Calculate total purchases and average price for each month
    result = {}
    for month, purchases in monthly_data.items():
        total_purchases = sum(info['data_points'] for info in purchases)
        avg_price = sum(info['avg_price_in_cents'] * info['data_points'] for info in purchases) / total_purchases
        result[month] = {'total_purchases': total_purchases, 'avg_price': avg_price}
    
    # Find the month with maximum purchases and lowest average price
    max_purchases_month = max(result, key=lambda m: result[m]['total_purchases'])
    lowest_avg_price_month = min(result, key=lambda m: result[m]['avg_price'])
    
    return max_purchases_month, lowest_avg_price_month

# Example usage:
if __name__ == "__main__":
    with open('test.json', 'r') as file:
        json_data = file.read()

    max_purchases_month, lowest_avg_price_month = analyze_purchase_data(json_data)
    print("Month with maximum purchases:", max_purchases_month)
    print("Month with lowest average price:", lowest_avg_price_month)
