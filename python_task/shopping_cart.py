# Part A: Spot the Bug
def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart
print(add_item_buggy("apple"))
print(add_item_buggy("banana"))
print(add_item_buggy("milk", cart=["bread"]))
print(add_item_buggy("eggs"))
 


# Part B: Fix It
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# Part C: Build the Cart
def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}
def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})
def update_price(price_tuple, new_price):
    # Tuples are immutable, so item assignment is not supported.
    # This raises a TypeError instead of changing the tuple.
    price_tuple[0] = new_price
def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]
    discount_amount = subtotal * (cart["discount"] / 100)
    return subtotal - discount_amount
def main():
    cart1 = create_cart("Ashrith", discount=10)
    cart2 = create_cart("Priya")
    add_to_cart(cart1, "Laptop", 50000, 1)
    add_to_cart(cart1, "Mouse", 500, 2)
    add_to_cart(cart2, "Notebook", 50, 5)
    print("Cart 1 items:", cart1["items"])
    print("Cart 2 items:", cart2["items"])
    print(f"{cart1['owner']}'s total: {calculate_total(cart1)}")
    print(f"{cart2['owner']}'s total: {calculate_total(cart2)}")
    price_info = ("Laptop", 50000)
    try:
        update_price(price_info, 45000)
    except TypeError as e:
        print(f"Cannot update tuple: {e}")
if __name__ == "__main__":
    main()


    
# ---- Discussion Points ----
# 1. discount=0 is safe because integers are immutable; each call gets its own value and cannot be changed in place. 
#    cart=[] is dangerous because the same list object is reused across every call that skips the cart argument,
#    so it silently accumulates state between calls.
#
# 2. Rebinding means pointing a variable at a new object (x = x + [1]).
#    Mutating means changing the existing object in place (x.append(1)).
#    Rebinding does not affect other variables pointing at the old object;
#    mutating does, since they still share the same object.
#
# 3. Mutable: list, dict, set.
#    Immutable: tuple, str, int.
#
# 4. Yes. A list passed into a function is passed by reference, so the function and the caller point to the same object. 
#    Any mutation inside the function is visible outside it too.
