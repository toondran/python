# 개인정보를 포맷 문자열로 출력
# 주민등록증(identification card)

name = input('이름 입력 : ')
user_id = input('아이디 입력 : ')
pw = input('비밀번호 입력 : ')
pw_hidden = "*" * len(pw)
id_card1 = input('주민번호 앞자리 입력 : ')
id_card2 = input('주민번호 뒷자리 입력 : ')
id_card_hidden = id_card2[0] + ('*' * 6)

print('=' * 30)
print("이름 {}".format(name))
print("아이디 {}".format(user_id))
print("비밀번호 {}".format(pw_hidden))
print("주민번호 {0}-{1}".format(id_card1, id_card_hidden))
print('=' * 30)