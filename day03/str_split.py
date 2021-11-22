#문자열 함수- 특별한 1차원 리스트

s="=banana, grape, apple"
x=s.split(',')
print(x)
print(x[0])

for i in x:
    print(i)

# 문자열 함수 - 특별한 1차원 리스트
s = "banana, grape, apple"
x = s.split(',')   #콤머(,)를 구분기호로 설정
print(x)  # ['banana', ' grape', ' apple']
print(x[0])
for i in x:
    print(i)

s2 = "a:b:c:d"
s2 = s2.split(':')
print(s2)
print(s2[-1])
print(s2[1:])

# 두 수를 동시에 입력 받아 더하기
n1, n2 = input("두 수 입력 : ").split()
add = int(n1) + int(n2)
print(add)

