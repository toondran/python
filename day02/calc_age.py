#나이 계산 프로그램

current_year = 2021
birth_year = int(input("태어난 년도를 입력하세요 : "))
#print(birth_year)

CURREN_YEAR = 2022
#나이 계산 : 나이 = 현재년도 - 태어난 년도
age = current_year - birth_year + 1

#출력
#print("당신이 나이는", age, "세 입니다.")
print("당신이 나이는 " + str(age) + "세 입니다.")
