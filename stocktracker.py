# Stock Portfolio Tracker (Works for Any Stock)

# Hardcoded dictionary of sample stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 125,
    "META": 290,
    "NFLX": 420,
    "NVDA": 480,
    "TCS": 3600,
    "INFY": 1450
}


def main():
    print("=== Stock Portfolio Tracker ===")

    print("\nAvailable predefined stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price}")

    total_value = 0
    portfolio = []

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        # If stock not in dictionary, ask user price
        if stock not in STOCK_PRICES:
            print(f"Price for {stock} not available.")
            try:
                price = float(input(f"Enter price for {stock}: "))
            except ValueError:
                print("Invalid price. Try again.")
                continue
            STOCK_PRICES[stock] = price  # store new stock
        else:
            price = STOCK_PRICES[stock]

        # Get quantity
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Invalid quantity. Enter a number.")
            continue

        value = qty * price
        total_value += value

        portfolio.append((stock, qty, price, value))

    # Summary
    print("\n=== Portfolio Summary ===")
    print(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value'}")
    print("-" * 40)

    for stock, qty, price, value in portfolio:
        print(f"{stock:<10}{qty:<10}${price:<10}${value}")

    print("\nTotal Portfolio Value: $", total_value)


if __name__ == "__main__":
    main()
