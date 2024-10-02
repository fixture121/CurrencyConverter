import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    try:
        base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
        response = requests.get(base_url)
        data = response.json()

        if response.status_code != 200 or data.get('result') != 'success':
            print("Failed to retrieve data. Please check your API key and base currency.")
            return None

        exchange_rate = data['conversion_rates'].get(target_currency)
        if exchange_rate is None:
            print(f"Invalid target currency: {target_currency}")
            return None

        return exchange_rate

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def is_valid_currency(currency):
    return currency.isalpha() and len(currency) == 3

def main():
    api_key = "cf6f46c55fd7ef88fd3653c4"
    while True:
        print("\nCurrency Converter")

        while True:
            base_currency = input("Enter the base currency (ex. USD): ").upper()
            if not is_valid_currency(base_currency):
                print("Invalid base currency. Please enter a 3-letter currency code.")
            else:
                break

        while True:
            target_currency = input("Enter the target currency (ex. EUR): ").upper()
            if not is_valid_currency(target_currency):
                print("Invalid target currency. Please enter a 3-letter currency code.")
            else:
                break

        while True:
            try:
                amount = float(input(f"Enter amount in {base_currency}: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            print(f"{amount} {base_currency} is equal to {converted_amount: .2f} {target_currency}")

        choice = input("\nDo you want to convert another amount? (y/n): ").lower()
        if choice not in ['y'.lower(), 'yes'.lower()]:
            print("Exiting Currency Converter app. Goodbye!")
            exit()

if __name__ == "__main__":
    main()
