# 리스트를 매개변수로 새로운 리스트 만들기

def times(a):
    li = []   # 새로운 빈 리스트
    for i in a:
        li.append(i * 4)
    return li

v = [5, 9, 3, 8]
print(times(v))