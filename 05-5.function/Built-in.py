### 내장 함수 ###

#! abs(x)
# 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 리턴하는 함수
# >>> abs(-3) 
# 3

#! all(x)
# 반복 가능한(iterable) 데이터를 x를 입력 값으로 받으며 
# 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.

# 반복가능한 데이터란 for문에서 사용 가능한 자료형을 의미한다.(리스트, 튜플, 문자열, 딕셔너리, 집합)
all([1,2,3]) # True
all([1,2,3,0]) # False ( 02-7장 )
all([]) # True >> 입력 인수가 빈 값인 경우에는 True를 리턴한다. 

#! any(x)
# 반복 가능한(iterable) 데이터를 x를 입력 값으로 받으며 
# 이 x의 요소 중 하나라도 참이 있면 True, x가 모두 거짓일 때 False를 리턴한다. // all(x)의 반대

any([1,2,3,0]) # True 
any([0, ""]) # False
any([]) # False

#! chr(i)
# 유니코드 숫자값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수이다.

chr(97) # 'a'
chr(44032) # '가'

#! dir
# 객체가 지닌 변수나 함수를 보여 주는 함수이다.

dir([1,2,3])
dir({'1':'a'})

#! divmod(a, b)
# 2개의 숫자를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플로 리턴하는 함수이다.

divmod(7, 3)
# (2, 1)

#! enumerate
# 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
# 보통 for문과 함께 사용한다.

for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)

# 0 body
# 1 foo
# 2 bar >> 출력값

# 순서 값과 함께 body, foo, bar가 순서대로 출력된다.
# enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
# for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때
# enumerate 함수를 사용하면 매우 유용하다.

#! eval(expression)
# 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수이다.

eval('1+2')
# 3
eval("'hi' + 'a'")
# 'hia'
eval('divmod(4,3)')
# (1,1)

#! filter
# filter(func, iterable)
# 첫 번째 인수로 함수를, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
# 반복 가능한 데이터(iterable)의 요소 순서대로 함수(func)를 호출했을 때 반환 값이 참인 것만 묶어서 리턴한다.

def positive(l): # 리스트를 입력으로 받아 각각의 요소를 판별해서 양수 값만 리턴하는 함수이다.
  result = [] 
  for i in l:
    if i > 0:
      result.append(i)
  return result
print(positive([1,-3,2,0,-5,6])) # [1,2,6] >> 결괏값

def positive(x):
  return x > 0
print(list(filter(positive, [1,-3,2,0,-5,6]))) # [1,2,6] >> 결괏값

# lambda를 사용하면 더 간단하게 사용 가능하다.
# >>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])) # [1,2,6] >> 결괏값

#! hex
# 정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수이다.

hex(234)
# '0xea'

#! id(object)
# 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 리턴하는 함수이다.

a = 3 
id(3)
# 135072304
id(a)
# 135072304
b = a
id(b)
# 135072304 // 값이 모두 동일하다.

id(4) # 값이 다르다

#! input([prompt])
# 사용자 입력을 받는 함수이다. 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.
# [] 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다.

a = input()
b = input("입력하세요 : ")

#! int(x)
# 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다. // 정수는 그대로 리턴한다.

int('3')
# 3
int(3.4)
# 3

# int(x, radix)
# radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다.
# 2진수로 표현된 '11'의 10진수 값은 다음과 같이 구할 수 있다.
int('11', 2)
# 3
int('1A', 16)
# 26

#! isinstance(object, class)

#! len(s)

#! list(iterable)

#! map(f, iterable)

#! max(iterable)

#! min(iterable)

#! oct(x)

#! open(file, [mode])

# w 쓰기모드로 파일 열기
# r 읽기모드로 파일 열기
# w 추가 모드로 파일 열기
# b 바이너리 모드로 파일 열기 (w, r, a와 함께 사용한다.)

#! ord(ㅊ)

#! pow(x, y)

#! range([start,] stop [,step])

#! round(number[,ndigits]) 
# []안의 값은 생략 가능하다.

#! sorted(iterable) 
# 리스트 자료형에도 sort함수가 있다. 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 리턴하지는 않는다.

#! str(object)

#! sum(iterable)

#! tuple(iterable)

#! type(object)

#! zip(*iterable)
# *iterable : 반복가능한 데이터 여러 개를 입력할 수 있다는 의미이다.