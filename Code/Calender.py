from datetime import datetime
from calendar import month


def get_calendar():
    # Get the current month and year
    now = datetime.now()
    month_num, year = now.month, now.year

    # Get the calendar for the current month and year
    calendar = month(theyear=year, themonth=month_num)
    return calendar


if __name__ == '__main__':
    # Get the calendar for the current month and year
    result = get_calendar()

    # Print the calendar
    print(result)
