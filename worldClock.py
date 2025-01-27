
# world clock displays the current time for multiple cities
import pytz
from datetime import datetime

# Dictionary of cities and their time zone

cities = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
}


def get_current_time(city):
    try:
        tz = pytz.timezone(cities[city])
        local_time = datetime.now(tz)
        return local_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    except KeyError:
        return f"city'{city}' not found in list "


def main():
    while True:
        print("\nWorld Clock")
        print("---------------")

        for city in cities:
            current_time = get_current_time(city)
            print(f"{city}:{current_time}")

        choice = input("\nEnter a city to add or 'q' to quit: ")

        if choice == 'q':
            break
        else:
            cities[choice] = input(f"Enter the time zone for {choice}: ")


if __name__ == '__main__':
    main()
