from datetime import datetime, date, timedelta

def get_days_from_today(date):
    str_to_date=datetime.strptime(date, "%d-%m-%Y").date()
    today_date=datetime.today().date()
    if str_to_date>today_date:
        days_ahead=str_to_date-today_date
    else:
        days_ahead=today_date-str_to_date
    return days_ahead.days
    
print(get_days_from_today("23-7-2026"))