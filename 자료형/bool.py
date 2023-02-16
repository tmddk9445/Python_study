# 불 자료형

# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
# 불 자료형은 True - 참, False - 거짓의 값만을 가질 수 있다. 
# True, False는 파이썬의 예약어로 첫문자를 항상 대문자로 사용해야 한다.

a = True
b = False

print(type(a))
print(type(b)) # <class 'bool'> >> 결괏값 // type(x)는 x의 자료형을 확인하는 파이썬의 내장 함수이다.

# 불 자료형은 조건문의 리턴 값으로 사용된다.
print( 1 == 1 ) # True >> 결괏값
print( 2 > 1 ) # True >> 결괏값
print( 2 < 1 ) # False >> 결괏값

# 자료형에도 참과 거짓이 있다.
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 (" ", [], (), {}) 거짓이 된다.
# 숫자에서는 그 값이 0일 때 거짓이 된다. // None도 거짓을 뜻한다.

a =[1,2,3,4]
while a:
  print(a.pop()) # a가 참인 경우에 a.pop()을 계속 실행하여 출력하라는 의미이다. 
  # a.pop() 리스트 a의 마지막 요소를 끄집어내는 함수이므로 리스트 안에 요소가 존재하는 한 마지막 요소를 계속 꺼낸다.
# 4
# 3
# 2
# 1 >> 결괏값

if[]:
  print("참")
else:
  print("거짓") # 거짓 >> 결괏값

if[1,2,3]:
  print("참")
else:
  print("거짓") # 참 >> 결괏값

### 불 연산

print(bool('python')) # True >> 결괏값
print(bool('')) # False >> 결괏값

print(bool([1,2,3])) # True >> 결괏값
print(bool([])) # False >> 결괏값

print(bool(0)) # False >> 결괏값
print(bool(3)) # True >> 결괏값




