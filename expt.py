# import datetime
#
# # Get the current date and time
# current_time = datetime.datetime.now()
#
# # Format the current time as a string
# current_time_str = current_time.strftime("%H:%M:%S")
#
# # Print the current time
# print("Current time:", current_time_str)

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta (days=1)
tomorrow = today + datetime.timedelta(days=1)
today_str = today.strftime("%Y-%m-%d")
yesterday_str = yesterday.strftime("%Y-%m-%d")
tomorrow_str = tomorrow.strftime("%Y-%m-%d")
print("Today's date:", today_str)
print("Yesterday's date:", yesterday_str)
print("Tomorrow's date:", tomorrow_str)