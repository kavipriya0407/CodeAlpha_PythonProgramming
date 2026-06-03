stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found!")

print("Total Investment Value: $", total)
