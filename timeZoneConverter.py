
# Time Zone Converter :converts times between different time zones
import datetime
import pytz


def convert_timeZone():
    # Get the current time in UTC
    utc_time = datetime.datetime.now(pytz.utc)

    # Display available time zone
    print("Availabel time zone:")
    for zone in pytz.all_timezones:
        print(zone)

    # Input time zone from the user
    user_timezone = input("Enter your time zone :")

    try:
        # Get the user's time zone
        user_timezone = pytz.timezone(user_timezone)

        # Convert the UTC time to the user time zone
        converted_time = utc_time.astimezone(user_timezone)

        # Display the converted time
        print("Current time in", user_timezone, ":",
              converted_time.strftime("%Y-%m-%d-%H-%M-%S %Z"))

    except pytz.exceptions.UnknowTimeZoneError:
        print("Invalid time zone . pleas enter a valid time zone.")


if __name__ == "__main__":
    convert_timeZone()
