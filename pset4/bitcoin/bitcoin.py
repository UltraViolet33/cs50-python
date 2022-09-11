import sys
import requests


def main():

    try:
        number_bitcoins = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing Command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response_api = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        response_api = response_api.json()
    except requests.RequestException:
        sys.exit("Error")

    rate_bitcoins = response_api["bpi"]["USD"]["rate_float"]
    cost_bitcoins = number_bitcoins * rate_bitcoins
    print(f"${cost_bitcoins:,.4f}")


if __name__ == "__main__":
    main()
