# All Together Now
"""
while repeat menu
    get choice
    if choice == i
        display notice
    else if choice == c
        while repeat getting number_products
            if number_products < 0
                display Invalid input
                keep repeating
            else
                break

        while repeat getting price
            if price <= 0
                display Invalid input
                keep repeating
            else
                break

        if number_products <= 5
            normal price
        else
            90% price

        display total price

    else if choice == q
        end the repeating
        display Farewell
    else
        display Invalid choice
"""
is_quit = False
while not is_quit:
    print("Menu:\n(I)nstructions\n(C)alculate\n(Q)uit")
    choice = input("Choice: ").lower()

    if choice == "i":
        print("Enter the number of products you want to buy and your chosen price.\n"
              "If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
    elif choice == "c":

        number_products = 0
        is_num_correct = False
        while not is_num_correct:
            number_products = int(input("Number of products: "))
            if number_products < 0:
                is_num_correct = False
                print("Invalid input")
            else:
                break

        price = 0.0
        is_price_correct = False
        while not is_price_correct:
            price = float(input("Price: "))
            if price <= 0:
                is_price_correct = False
                print("Invalid input")
            else:
                break

        if number_products <= 5:
            total_price = number_products * price
        else:
            total_price = number_products * price * 0.9

        print(f"{number_products} x ${price} products = ${total_price}")
    elif choice == "q":
        is_quit = True
        print("Farewell")
    else:
        print("Invalid choice")
