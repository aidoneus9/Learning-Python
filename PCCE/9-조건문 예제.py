#1
country_name = input('국가명을 입력하세요:')
# print(country_name)

if country_name == 'Korea' or country_name == 'korea':
    print("한국입니다.")
# if country_name in ['Korea', 'korea']: # 집합으로도 가능, 여러 개 중에 일치하는 게 있는지 확인
# if country_name == 'America' or 'america': 의 경우 T/F or 'america'가 됨(연산 불가)
# 위에서 ('America' or 'america')라고 괄호로 묶은 경우에도, or은 논리연산자이므로 T/F만 가능
elif country_name == 'America' or country_name == 'america':
    print("미국입니다.")
elif country_name == 'Japan' or country_name == 'japan':
    print("일본입니다.")
else:
    print("지원하지 않는 국가입니다")

#2
score = int(input('점수를 입력하세요:'))
# string의 number 변환? int, float

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#3
math, eng = input('수학점수와 영어점수를 띄어쓰기로 구분해서 입력하세요:').split(" ")
math = int(math)
eng = int(eng)

if math < 40 or eng < 40: #과락을 먼저 처리하면 쉬울 것 같아서
    print("과락")
else: 
    if math >= 90 and eng >= 90:
        print('Perfect!')
    elif math >= 90:
        print('수학천재!')
    elif eng >= 90:
        print('영어천재!')
    else:
        print('준수함')