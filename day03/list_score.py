# 점수의 합계와 평균, 최고 점수, 최저 점수

score = [70, 80, 90, 20, 40]
count = len(score) # 개수
sum_v = 0
avg = 0.0

# 합계 계산
for i in score:
    sum_v += i

# 평균 계산
avg = sum_v / count

# 최고 점수
max_v = score[0]   #최대값 설정
for i in score:
    if max_v < i:
        max_v = i

# 최저 점수
min_v = score[0]
for i in score:
    if min_v > i:
        min_v = i

print("개수 :", count)
print("합계 :", sum_v)
print("합계 :", sum(score))
print("평균 :", avg)
print("최고 점수 :", max_v)
print("최고 점수 :", max(score))
print("최저 점수 :", min_v)