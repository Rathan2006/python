products={}
product=""
while 1:
    print("<<<Type enq if you want to check products and prices>>> \n")
    product=input("Enter the product name:")
    if product=="enq":
        break;
    price=float(input(f"Enter the price of {product}:"))
    products.update({product:price})
while 1:
    print("<<<Type Exit if you want to Exit>>> \n")
    product=input("Enter the product name:")
    if product=="Exit":
        break;
    print(products.get(product))
print("Exited...")