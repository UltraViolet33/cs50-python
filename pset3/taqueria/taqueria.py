menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def get_order():

    total_price = 0

    while True:
        try:
            item = input("Item: ")
            item = item.title()
            print(item)
            total_price += menu[item]
            total_price_str = "{:.2f}".format(total_price)
            print(f'${total_price_str}')
        except KeyError:
            pass
        except EOFError:
            print('\n')
            break


get_order()
