### 함수 ###

### 파이썬 함수의 구조

# def 함수명 (매개변수) :
#   <수행할 문장1>
#   <수행할 문장2>...

# def는 함수를 만들 때 사용하는 예약어이다.

def add(a, b):
  return a + b

a = 3
b = 4
c = add(a, b)
print(c) # 7 >> 결괏값

# 매개변수 : 이 함수에 입력으로 전달되는 값을 받는 변수이다.
# >> 함수에 전달된 값을 저장하는 변수
# 인수 : 함수를 호출할 때 전달하는 입력값이다.
# >> 함수에 전달하는 값

def add(a, b): # a, b는 매개변수
  return a + b

print(add(3, 4)) # 3, 4는 인수

# 입력값 = 함수의 인수, 파라미터, 매개변수
# 리턴값 = 결괏값, 출력값, 반환 값, 돌려주는 값

# 함수는 들어온 입력값을 받아 어떤 처리를 하여 적절한 리턴값을 돌려준다.

### 일반적인 함수 ###

# def 함수이름(매개변수):
#   수행할 문장
#   ...
#   return 리턴값

def add(a, b):
  result = a + b
  return result # 2개의 입력값을 받아서 서로 더한 결괏값을 리턴한다.

a = add(3,4)
print(a) # 7 >> 결괏값

# 리턴값이 있는 함수의 사용법
# 리턴값을 받을 변수 = 함수이름(입력인수1, 입력인수2)

### 입력값이 없는 함수 ###

def say():
  return 'Hi'

a = say()
print(a) # Hi >> 결괏값

# a = say()처럼 작성하면 a에 "Hi"라는 문자열이 대입된다.

# 입력값이 없는 함수의 사용법
# 리턴값을 받을 변수 = 함수이름()

### 리턴값이 없는 함수 ###

def add(a, b):
  print("%d, %d의 합은 %d입니다." %(a, b, a+b))

add(3, 4) # 3, 4의 합은 7입니다. >> 결괏값

# 리턴값이 없는 함수의 사용법
# 함수이름(입력인수1, 입력인수2)

a = add(3, 4)
print(a) # None >> 리턴값이 없다. // None은 거짓을 나타내는 자료형이다.

# print문은 함수의 구성 요소 중 하나인 수행할 문장에 해당하는 부분일 뿐이다.
# 리턴값은 오직 return 명령어로만 돌려받을 수 있다.

### 입력값도 리턴값도 없는 함수

def say():
  print("Hi")

say() # Hi >> 결괏값

# 입력값도 리턴값도 없는 함수의 사용법
# 함수이름()

### 매개변수 지정하여 호출하기 ###
def sub(a, b):
  return a - b

result = sub(a=7, b=3) # a에 7, b에 3을 전달
print(result) # 4 >> 결괏값

result = sub(b=5, a=3) # b에 5, a에 3을 전달
print(result) # -2 >> 결괏값

### 입력값이 여러개일 때 ###

# def 함수이름(*매개변수):
#   수행할 문장

def add_many(*args): # 매개변수 이름 앞에 * 를 붙이면 입력값을 전부 모아서 튜플로 만들어 준다.
  result = 0
  for i in args:
    result = result + i
  return result

result = add_many(1,2,3)
print(result) # 6 >> 결괏값

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result) # 55 >> 결괏값

def add_mul(choice, *args):
  if choice == "add":
    result = 0
    for i in args:
      result = result + i
  elif choice == "mul":
    result = 1
    for i in args:
      result = result * i
  return result

result = add_mul('add', 1,2,3,4,5)
print(result) # 15 >> 결괏값

result = add_mul('mul', 1,2,3,4,5)
print(result) # 120 >> 결괏값

### 키워드 매개변수 kwargs ###

# 키워드 매개변수를 사용할 때는 매개변수 앞에 별 두개(**)를 붙인다.

def print_kwargs(**kwargs):
  print(kwargs)

print_kwargs(a=1) # {'a': 1} >> 결괏값
print_kwargs(name='foo', age=3) # {'name': 'foo', 'age': 3} >> 결괏값

# 함수의 입력값으로 a=1이 사용되면 kwargs는 {'a':1}이라는 딕셔너리가 된다.
# **kwargs 처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고
# 모든 key = value형태의 입력값이 그 딕셔너리에 저장된다.

### 함수의 리턴값은 언제나 하나이다. ###

def add_and_mul(a,b):
  return a+b, a*b

result = add_and_mul(3,4) # 오류는 발생하지 않는다.
print(result) # (7, 12) >> 결괏값
# 함수의 리턴값은 2개가 아니라 언제나 1개이다. 
# a+b, a*b는 튜플값 하나인 a+b, a*b로 리턴된다.

# 튜플 값을 2개의 값으로 분리하고 싶은 경우
result1, result2 = add_and_mul(3,4)
print(result1, result2) # 7 12 >> 결괏값

def add_and_mul(a,b):
  return a+b
  return a*b

result = add_and_mul(2,3)
print(result) # 5 >> 결괏값 // 두 번째 return문인 return(a*b)는 실행되지 않았다.

# 함수는 return문을 만나는 순간 리턴값을 돌려준 다음 함수를 빠져나가게 된다.

# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.

def say_nick(nick):
  if nick == "바보":
    return
  print("나의 별명은 %s입니다." % nick)

# 위의 함수는 리턴값이 없다. (문자열을 출력한다는 것과 리턴 값이 있다는 것은 다르다!)
# 함수의 리턴 값은 오로지 return문에 의해서만 생성된다.

say_nick("야호") # 나의 별명은 야호입니다. >> 결괏값
say_nick("바보") # 결괏값 X

#! 매개변수에 초깃값 미리 설정하기

def say_myself(name, age, man=True):
  print("나의 이름은 %s입니다." % name)
  print("나이는 %d입니다." % age)
  if man:
    print("남자입니다.")
  else:
    print("여자입니다.")

# say_myself 함수는 3개의 매개변수를 받아서 
# 마지막 인수인 man이 True이면 "남자입니다.", False이면 "여자입니다."를 출력한다.

say_myself("이승아", 27)
say_myself("이승아", 27, True) # 결괏값이 동일하다.

# 나의 이름은 이승아입니다.
# 나이는 27입니다.
# 남자입니다. >> 결괏값

say_myself("이승아", 27, False)

# 나의 이름은 이승아입니다.
# 나이는 27입니다.
# 여자입니다.

# def say_myself(name, man=True, age):
#   print("나의 이름은 %s입니다." % name)
#   print("나이는 %d입니다." % age)
#   if man:
#     print("남자입니다.")
#   else:
#     print("여자입니다.")

# say_myself("이승아", 27) # 오류 발생 : SyntaxError: non-default argument follows default argument

# 위 오류 메시지는 초깃값이 없는 매개변수 (age)는 초깃값이 있는 매개변수(man) 뒤에 사용할 수 없다는 뜻이다.
# 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓아야한다.
# 파이썬 인터프리터가 27을 man 매개변수와 age매개변수 중 어느 곳에 대입해야 할지 판단하기 어렵다.

#component 함수 안에서 선언한 변수의 효력 범위

a = 1 # a 변수 생성, 1 대입
def vartest(a):
  a = a + 1 # vartest함수 : a를 입력 받아 1 더해주고 결괏값은 리턴하지 않는다.
vartest(a) # vartest함수에 입력값으로 a를 주었다.
print(a) # 1 >> 결괏값

# 함수 안에서 사용하는 매개변수는 함수 안에서만 사용하는 "함수만의 변수"이기 때문에
# def vartest(a)에서 입력값을 전달받는 매개변수 a는 
# 함수 안에서만 사용하는 변수이지 함수 밖의 변수 a와 전혀 상관이 없다.

def vartest(hello):
  hello = hello + 1

#  vartest함수는 다음처럼 매개변수 이름을 hello로 바꾸어도 이전의 vartest 함수와 완전히 동일하게 동작한다.
#  함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다.

def vartest(a):
  a = a + 1

vartest(3)
print(a) # None >> 결괏값

# vartest(3)을 수행하면 vartest 함수 안에서 a는 4가 되지만 함수를 호출하고 난 뒤에
# print(a) 문장은 오류가 발생하게 된다.
# print(a)에서 사용한 a 변수를 찾을 수 없다.

#component 함수 안에서 함수 밖의 변수를 변경하는 방법

# vartest라는 함수를 사용해서 함수 밖의 변수 a를 1만큼 증가시키는 방법

# 1. return 사용하기

a = 1
def vartest(a):
  a = a + 1
  return a

a = vartest(a)
print(a) # 2 >> 결괏값

# vartest 함수는 입력으로 들어온 값에 1을 더한값을 리턴하도록 변경했다.
# a = vartest(a)라고 작성하면 a에는 vartest 함수의 리턴값이 대입된다. // 함수 안의 a매개변수 != 함수 밖의 a

# 2. global 명령어 사용하기

a = 1
def vartest():
  global a
  a = a + 1
vartest()
print(a) # 2 >> 결괏값

#component Lambda

# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

# 사용법
# 함수명 = lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b : a+b
result = add(3,4)
print(result) # 7 >> 결괏값 // lambda로 만든 함수는 return 명령어가 없어도 표현식의 결괏값을 리턴한다.

def add(a,b):
  return a + b
result = add(3,4)
print(result) # def를 사용한 이 함수와 동일하다.




