import calendar

# 요일의 길이를 세 글자로 변경
calendar.setfirstweekday(calendar.SUNDAY)  # 일요일부터 시작하도록 설정
day_names = list(calendar.day_abbr)  # 기존의 요일명 리스트를 가져옴
day_names[0] = 'Sun'  # 첫 번째 요일을 'Sun'으로 변경
day_names[1] = 'Mon'  # 두 번째 요일을 'Mon'으로 변경
day_names[2] = 'Tue'  # 세 번째 요일을 'Tue'으로 변경
day_names[3] = 'Wed'  # 네 번째 요일을 'Wed'으로 변경
day_names[4] = 'Thu'  # 다섯 번째 요일을 'Thu'으로 변경
day_names[5] = 'Fri'  # 여섯 번째 요일을 'Fri'으로 변경
day_names[6] = 'Sat'  # 일곱 번째 요일을 'Sat'으로 변경

# 달력 생성
cal = calendar.TextCalendar(calendar.SUNDAY)  # 일요일부터 시작하는 TextCalendar 객체 생성
cal.setfirstweekday(calendar.SUNDAY)  # 일요일부터 시작하도록 설정
cal.day_name = day_names  # 달력의 요일명을 변경한 리스트로 설정

# 달력 출력
year = 2023
month = 10
print(cal.formatmonth(year, month))
