# 지역변수

def one_up():
    x = 1     #지역변수(블럭을 벗어나면 메모리에서 해제)
    x += 1
    return x

print(one_up())  # 2
print(one_up())
#print(x)