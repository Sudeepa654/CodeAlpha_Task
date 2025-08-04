# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 135,
    "MSFT": 330
}

def display_available_stocks():
    print("\nAvailable Stocks and Prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

def get_user_portfolio():
    portfolio = {}
    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found. Please enter a valid symbol from the list.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock} you own: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid integer quantity.")
    return portfolio

def calculate_investment(portfolio):
    total_value = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_value += value
        print(f"{stock}: {qty} shares x ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total_value}")
    return total_value

def save_to_file(portfolio, total_value, file_type='txt'):
    filename = "portfolio." + file_type
    try:
        with open(filename, "w") as file:
            if file_type == 'csv':
                file.write("Stock,Quantity,Price,Value\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    file.write(f"{stock},{qty},{price},{value}\n")
                file.write(f",,,\nTotal,,,{total_value}")
            else:
                file.write("Your Stock Portfolio:\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
                file.write(f"\nTotal Investment Value: ${total_value}")
        print(f"\nPortfolio saved successfully as '{filename}'")
    except Exception as e:
        print("Error saving file:", e)

def main():
    print("=== Simple Stock Portfolio Tracker ===")
    display_available_stocks()
    portfolio = get_user_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    total_value = calculate_investment(portfolio)

    save = input("\nWould you like to save this report? (yes/no): ").lower()
    if save == 'yes':
        file_type = input("Choose file type (txt or csv): ").lower()
        if file_type not in ['txt', 'csv']:
            print("Invalid file type. Defaulting to txt.")
            file_type = 'txt'
        save_to_file(portfolio, total_value, file_type)
    print("\nThank you for using the Stock Portfolio Tracker!")


main()