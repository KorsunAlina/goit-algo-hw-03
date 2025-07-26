from datetime import datetime, date, timedelta

def get_days_from_today(date):
   try:
    if "." in date: # replace incorrect separator "." for "-"
        correct_date_format=date.replace(".", "-")
        str_to_date=datetime.strptime(correct_date_format, "%Y-%m-%d").date()
    else:
            str_to_date=datetime.strptime(date, "%Y-%m-%d").date()
    
    today_date=datetime.today().date()
    days_ahead=today_date-str_to_date
    
    return days_ahead.days
   
   except ValueError: # check incorrect date format
       return "Incorrect date format."
    
print(get_days_from_today("2026.07.25"))