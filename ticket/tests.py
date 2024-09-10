from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format it to display day, month, year, and time
formatted_time = now.strftime("%d %B %Y, %H:%M:%S")

print(formatted_time)
