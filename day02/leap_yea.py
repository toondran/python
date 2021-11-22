# 윤년(leap_year)을 판별하는 프로그램
# 윤년은 4년마다 오고, 100으로 나누어 떨어지지 않으나 400년 마다 온다.

year = int(input("년도 입력 : "))

if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
    print(str(year) + "년은 윤년입니다.")
else:
    print(str(year) + "년은 평년입니다.")
