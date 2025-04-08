import os

all_price = {}

end_bid = False

while not end_bid:
    name = input("What is your name?: ")
    price = int(input("What is your price?: "))
    all_price[name] = price
    if input("is there any price: ").lower() == "no":
        end_bid = True  
    os.system('cls' if os.name == 'nt' else 'clear')

max = 0
for bidder in all_price:
    bid_ammount = all_price[bidder]
    if bid_ammount > max:
        max = bid_ammount
        highest = bidder

print(f'The highest bidder is {highest} and price is {max} ')