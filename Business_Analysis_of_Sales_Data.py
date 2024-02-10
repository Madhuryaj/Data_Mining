def best_selling_product(sales_data):
    max_quantity = 0
    best_product = None
    for i in sales_data:
        quantity_sold = i[3]
        if quantity_sold > max_quantity:
            max_quantity = quantity_sold
            best_product = i[1]
    return best_product


def avg_unit_price(sales_data):
    Total_price = 0
    Total_quantity = 0
    for i in sales_data:
        quantity = i[3]
        price = i[2]
        Total_price = Total_price + quantity * price
        Total_quantity = Total_quantity + i[3]
    print("Total_price", Total_price)
    print("Total_quantity", Total_quantity)
    return Total_price / Total_quantity


def products_below_avg_price(sales_data, avg_price):
    list_of_below_avg_products = []
    for i in sales_data:
        if i[2] < avg_price:
            list_of_below_avg_products.append(i[1])
    return (list_of_below_avg_products)


sales_data = [
    (1, 'Product A', 10.0, 50, None),
    (2, 'Product B', 8.0, 75, None),
    (3, 'Product C', 12.0, 30, None),
    (4, 'Product D', 15.0, 20, None),
    (5, 'Product E', 5.0, 100, None),
    (6, 'Product F', 18.0, 40, None),
    (7, 'Product G', 7.5, 60, None),
    (8, 'Product H', 11.0, 35, None),
    (9, 'Product I', 9.0, 80, None),
    (10, 'Product J', 14.0, 25, None),
]

print(best_selling_product(sales_data))
print(avg_unit_price(sales_data))
avg_price = 10.5
print(products_below_avg_price(sales_data, avg_price))
