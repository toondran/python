# 학생의 성적 합계 및 평균
# 대응 서식 문자 - 정수 : %d, 실수 : %f, 문자열 : %s
student = [
    {'name':'김하나', 'kor':80, 'math':70, 'eng':90},   #1명의 세 과목의 점수
    {'name':'이두울', 'kor':60, 'math':50, 'eng':40},
    {'name':'박세엣', 'kor':90, 'math':90, 'eng':100}
]

# 개인별 총점과 평균
print(" 이름  총점 평균")
for s in student:
    sum_v = s['kor'] + s['math'] + s['eng']
    avg = sum_v / 3
    print("%s %d %.1f" % (s['name'], sum_v, avg))

# 과목별 총점과 평균
# sum_kor = 0  #국어 합계
# sum_math = 0
# sum_eng = 0

sum_subj=[0,0,0 ] #리스트 초기화 (위 정리)

for s in student:
    sum_subj[0] += s['kor']
    sum_subj[1] += s['math']
    sum_subj[2] += s['eng']

avg_kor = sum_kor / 3
avg_math = sum_math / 3
avg_eng = sum_eng / 3

print("국어 합계 : %d점" % sum_kor)
print("수학 합계 : %d점" % sum_math)
print("영어 합계 : %d점" % sum_eng)
print("국어 평균 : %.1f점" % avg_kor)
print("수학 평균 : %.1f점" % avg_math)
print("영어 평균 : %.1f점" % avg_eng)