#Coverts currency using live exchange rates using currency exchange api
import requests

def fetch_exchange_rates(base_currency="EUR"):
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key=[API_KEY]&base_currency={base_currency}]"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates")

    data = response.json()

    if not data.get("success", False):
        raise Exception("API did not return success")

    return data


def display_summary(data):
    print(f" Exchange Rate Summary")
    print(f"Date       : {data['date']}")
    print(f"Base       : {data['base']}")
    print(f"Timestamp  : {data['timestamp']}")
    print(f"Total Rates: {len(data['rates'])}")
    print()


def track_currency(data, target_currency):
    rates = data['rates']
    if target_currency not in rates:
        print(f"Currency {target_currency} not found.")
        return

    rate = rates[target_currency]
    print(f" 1 {data['base']} = {rate:.4f} {target_currency}")


def main():
    base = input("Enter base currency (default EUR): ").upper() or "EUR"
    target = input("Enter target currency (e.g., USD, GBP, LKR): ").upper()

    try:
        data = fetch_exchange_rates(base)
        display_summary(data)
        track_currency(data, target)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
