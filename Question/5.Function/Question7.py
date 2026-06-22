# 7. Create a function that prints today's date.

from datetime import date   
def print_today_date():
    today = date.today()
    print(f"Today's date is: {today}")
print_today_date()
