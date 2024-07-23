import calendar

def print_month_calendar(year, month):
    """Prints the calendar for a specific month and year."""
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)

year = 2024
month = 7
print_month_calendar(year, month)
