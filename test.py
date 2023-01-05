import datetime
date_string = "2018/08/09"

my_str = '2023-24-09' # 👉️ YYYY-DD-MM

date = datetime.datetime.strptime(my_str, '%Y-%d-%m')
print(date)  # 👉️ 2023-09-24 00:00:00