### if문 ###

money = True
if money :
    print("택시타기")
else :
    print("걸어가기") # 택시타기 >> 결괏값
# else 문은 if 문 없이 독립적으로 사용할 수 없다.

# if문을 만들 때는 if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에
# 들여쓰기를 해주어야 한다.

# money = True
# if money :
#     print("안녕")
# print("하세요")
#     print("하이") >> 들여쓰기 오류

# if 조건문:
    # 수행할 문장1
    # 수행할 문장2
    #     수행할 문장3 >> 들여쓰기 오류 : 들여쓰기는 언제나 같은 깊이로 해야 한다.

# 들여쓰기는 탭과 공백 모두 가능하며 둘 중에 하나를 통일해서 사용하는 것이 좋다.
# 조건문 뒤에는 반드시 콜론(:)이 붙는다. >> 파이썬 문법 구조

money = True
if money: # money : 조건문
    print('a')
# if 조건문에서 조건문이란 참과 거짓을 판단하는 문장이다.

### 비교연산자 ###

x = 3
y = 1
if x > y :
    print('a') # a >> 결괏값
if x < y :
    print('b') # 결괏값 X : False
if x == y :
    print('c') # 결괏값 X : False
if x != y :
    print('d') # d >> 결괏값

money = 2000
if money >= 3000:
    print('3000 이상')
else :
    print('3000 이상이 아닙니다.') # 3000 이상이 아닙니다. >> 결괏값

### and, or, not ###

x or y # x와 y 둘중에 하나만 참이어도 참이다.
x and y # x와 y 모두 참이어야 참이다.
not x # x가 거짓이면 참이다.

money = 2000
card = True
if money >= 3000 or card: # >=3000 : False, card : True >> True
    print('택시 타고가기')
else :
    print('걸어가기') # 택시 타고가기 >> 결괏값

### in, not in ###
# x in 리스트 
# x in 튜플
# x in 문자열

# x not in 리스트 
# x not in 튜플
# x not in 문자열

print(1 in [1,2,3]) # True >> 결괏값
print(1 not in [1,2,3]) # False >> 결괏값

print('a' in ('a', 'b', 'c')) # True >> 결괏값
print('j' not in 'python') # True >> 결괏값

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print("택시타기")
else :
    print("걸어가기") # 택시타기 >> 결괏값

# 조건문에서 아무 일도 하지 않게 설정하기

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    pass
else :
    print("카드 꺼내기") # 카드 꺼내기 >> 결괏값

# 다양한 조건을 판단하는 elif 

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print("택시타기")
else :
    if card :
        print("택시타기")
    else :
        print("걸어가기")  # 택시타기 >> 결괏값

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print("택시타기")
elif card :
    print("택시타기")
else :
    print("걸어가기")  # 택시타기 >> 결괏값 
# elif는 이전 조건문이 거짓일 때 수행된다. // elif는 개수에 제한 없이 사용할 수 있다.

# if문을 한 줄로 작성하기

if 'money' in pocket :
    pass
else :
    print("카드를 꺼내라") # 카드를 꺼내라 >> 결괏값 

if 'money' in pocket : pass
else : print("카드르 꺼내라") # 카드를 꺼내라 >> 결괏값 

### 조건부 표현식 ###

score = 60
message = ''
if score >= 60:
    message = "success" # 지역변수이기 때문에 안에서 사용할 수 없다.
else :
    message = "failure" # success >> 결괏값 

print(message)

# 조건부 표현식 표현 : 가독성에 유리하고 한 줄로 작성할 수 있다.
message = "success" if score >= 60 else "failure"
# 변수 = 조건문이 참인 경우의 값 if 조건문 else 조건문이 거짓인 경우의 값
print(message)




