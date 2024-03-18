import datetime

today = (datetime.datetime.today() + datetime.timedelta(days=7)).strftime('%d/%m/%Y')

print(today)