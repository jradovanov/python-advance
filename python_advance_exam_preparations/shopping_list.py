def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    bought_product = []

    for key, value in kwargs.items():
        if len(bought_product) == 5:
            break
        products = key
        price = value[0]
        quantity = value[1]
        total = price * quantity
        if budget >= total:
            budget -= total
            bought_product.append(f"You bought {products} for {total:.2f} leva.")

    return "\n".join(bought_product)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

