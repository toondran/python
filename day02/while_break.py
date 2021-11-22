# while ~  break문

"""
# 1부터 10까지 출력
i = 0
while True:
    i += 1
    #i++
    if i > 10:
        break
    print(i)
"""

# 키가 'y' 이면 "계속 반복", 'n' 이면 "반복 중단", 그 이외 키는 "정상 답변이 아님"
while True:
    key = input("반복을 계속할까요?(y/n) ")

    # 조건 처리
    if key == 'y' or key == 'Y':
        print("계속 반복")
    elif key == 'n' or key == 'N':
        print("반복 중단")
        break
    else:
        print("정상 답변이 아님")
