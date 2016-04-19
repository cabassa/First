def car_tax(price):
    result = 0
    if price < 20000:
        result = 0.5 * price
    elif price >= 20000 and price <= 50000:
        result = .10 * price
    else:
        result = 0.15 * price
    return result
