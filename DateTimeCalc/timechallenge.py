# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import datetime
import pytz

tz_dict = {"1": "Pacific/Truk",
           "2": "Poland",
           "3": "Pacific/Saipan",
           "4": "Pacific/Galapagos",
           "5": "Greenwich",
           "6": "Iceland",
           "7": "Hongkong",
           "8": "Europe/Volgograd",
           "9": "Australia/Tasmania",
           }

while True:
    print("Please select from the following timezones:")
    for tz in tz_dict.keys():
        print(tz + " - " + tz_dict[tz])

    select_timezone = input()

    if select_timezone == "0":
        break
    elif select_timezone in tz_dict.keys():
        timezone = pytz.timezone(tz_dict[select_timezone])
        timezone_time = datetime.datetime.now(tz=timezone)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        print("The time in {} is {} {}".format(timezone, timezone_time.strftime('%A %x %X %z'),
                                               timezone_time.tzname()))
        print("Local time is {}".format(local_time.strftime('%A %x %X %z')))
        print("UTC time in is {}".format(utc_time.strftime('%A %x %X %z')))
    else:
        print("Please only select from the above list")
