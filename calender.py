import calendar

# Create a TextCalendar instance
cal = calendar.TextCalendar(calendar.SUNDAY)

# Define the year and month you want to display
year = 2023
month = 10

# Generate and display the calendar for the specified year and month
print(cal.formatmonth(year, month))