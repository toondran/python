# 절대값 함수 구현하기
import math

# 절대값 알고리즘1
def myabs(x):
    if x < 0:
        return -x
    else:
        return x

# 절대값 알고리즘 2
def myabs2(x):
    y = x * x
    return int(math.sqrt(y))   # 제곱근

print(myabs(-3))    #3
print(myabs2(-3))   #3
print(abs(-3))      #3 내장함수