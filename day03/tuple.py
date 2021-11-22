#p146
#1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

"""
if "wife" in a:
    print("wife")
if "python" in a and "you" not in a:
    print("python")
if "shirt" not in a:
    print("shirt")
if "need" in a:
    print("need")
"""

#2
result = 0
count = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        count += 1
        result += i
    i += 1
print("합계 : ", result)
print("개수 : ", count)

# 3
print('=' * 30)
print('*' * 5)

# 직각 삼각형 모양
# while문
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

# for문
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end='')
    print()
print()

# 4

# 5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(total)
print(average)