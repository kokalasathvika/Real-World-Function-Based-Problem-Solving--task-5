def filter_premium_crops(price_list):
    premium = []
    
    for price in price_list:
        if price > 2000:
            premium.append(price)
    
    print("Premium Crops:", premium)

# Example
filter_premium_crops([1500, 2500, 3200, 1800])