# Stock Portfolio Tracker
# using Dictionaries for stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2750,
    "MSFT": 320,
    "AMZN": 3400
}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

portfolio = {}
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        if qty < 0:
            print("Quantity cannot be negative.")
            continue
    except ValueError:
        print("Please enter a valid integer for quantity.")
        continue
    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty

print("\nYour Portfolio:")
total_investment = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

save = input("Do you want to save the result? (yes/no): ").lower()
if save == "yes":
    format_choice = input("Save as (1) .txt or (2) .csv? Enter 1 or 2: ").strip()
    if format_choice == "1":
        filename = "portfolio.txt"
        with open(filename, "w") as f:
            f.write("Stock Portfolio:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"Saved to {filename}")
    elif format_choice == "2":
        filename = "portfolio.csv"
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Unit Price,Total Value\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
            f.write(f"Total Investment,,,{total_investment}\n")
        print(f"Saved to {filename}")
    else:
        print("Invalid choice. Not saved.")
else:
    print("Result not saved.")
    