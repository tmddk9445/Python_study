### 문자열 자료형 ###

# 문자열 자료형은 그 요솟값을 변경할 수 없다. immutable 자료형

#? 문자열 포맷 코드

# %s : 문자열
# %c : 문자 1개
# %d : 정수
# % % : Literal %

# 1. 정렬과 공백
# 2. 소수점 표현하기

#? format 함수를 사용한 포매팅

# >>> "I eat {0} apples".format(3)
# 'I eat 3 apples'

f = "I ate {0} apples. so I was for {day} days.".format(10, day =3)
print(f)

