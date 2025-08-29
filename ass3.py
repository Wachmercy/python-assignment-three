def calculate_discount(initial_price, discount_percent):
    discount_amount=final_price-initial_price
    discount_percent=initial_price*(discount_amount/100)
    final_price=initial_price - discount_amount
    if discount_percent>=20:
        return final_price
    else:
        initial_price
initial_price=float(input("Enter initial price: "))
discount_percent=float(input("Enter discount percent: "))
final_price=calculate_discount(initial_price,discount_percent)
if discount_percent>=20:
        print(f"final price wih discount: ")
else:
     print(f"final price with no discount: ")