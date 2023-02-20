### 예외 처리 ###

#component FileNotFoundError 오류

# 존재하지 않는 파일을 사용하려고 시도했을 때 발생하는 오류
# >>> f=open("나 없는 파일", 'r')

#component ZeroDivisionError 오류

# 0으로 다른 숫자를 나누는 경우
# >>> 4 / 0

#component IndexError 오류

# a = [1,2,3]
# a[4]
# a는 리스트 [1,2,3]이므로 a[4]는 a 리스트에서 얻을 수 없는 값이다.

#component 오류 예외 처리 기법

#! try, except문

# try:
#   ...
# except [발생오류 [as 오류변수]]:
#   ...

# >> try 블록 수행 중 오류가 발생하면 except 블록이 수행된다 
# try블록에서 오류가 발생하지 않는다면 except블록은 수행되지 않는다.

# except [발생오류 [as 오류변수]]: >> [] 기호는 괄호 안의 내용을 생략할 수 있다는 관례적인 표기법이다.

# 1. try, except 만 쓴ㄴ 방법

# try:
#   ...
# except:
#   ...

# 2. 발생 오류만 포함한 except문

# try:
#   ...
# except 발생오류:
#   ...

# 3. 발생오류와 오류변수까지 포함한 except문

# try:
#  ...
# except 발생오류 as 오류변수:
#  ...

# >> 이 경우는 두번째 경우에서 오류의 내용까지 알고 싶을 때 사용하는 방법이다.

try:
  4 / 0
except ZeroDivisionError as e:
  print(e)

#! try .. finally

# try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
# 보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.

try:
  f=open('foo.txt', 'w')
  # 무언가를 수행한다.
finally:
  f.close()
  #중간에 오류가 발생하더라도 무조건 실행된다. 
  # >> 예외 발생 여부와 상관없이 finally절에서 f.close()로 열린 파일을 닫을 수 있다.

#! 여러개의 오류처리하기

# try:
#   ...
# except 발생오류1:
#   ...
# except 발생오류2:
#   ...

# >> 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다.
try:
  a=[1,2]
  print(a[3]) # 인덱싱 오류가 먼저 발생했으므로 4/0으로 발생되는 ZeroDivisionError 오류는 발생하지 않는다.
  4/0
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")
except IndexError:
  print("인덱싱 할 수 없습니다.") # "list index out of range" 오류메시지 출력

try:
  a=[1,2]
  print(a[3])
  4/0
except (ZeroDivisionError, IndexError) as e:
  print(e)

#! try ... else

# try:
#   ...
# except [발생오류 [as 오류변수]]:
#   ...
# else: # 오류가 없을 경우에만 수행된다.
#   ...

try:
  age=int(input('나이를 입력하세요 : '))
except:
  print('입력이 정확하지 않습니다.')
else:
  if age <= 18:
    print('미성년자는 출입금지입니다.')
  else:
    print('환영합니다.')

#! 오류 회피하기

try:
  f=open('없는파일','r')
except FileNotFoundError:
  pass

#! 오류 일부러 발생시키기

# Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우
# (강제로 그렇게 하고 싶은 경우)

class Bird:
  def fly(self):
    raise NotImplementedError 
    # NotImplementedError 파이썬에 정의되어 있는 오류 
    # 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부로 오류를 일으키기 위해 사용한다.

# class Eagle(Bird):
#   pass

# eagle = Eagle()
# eagle.fly()

# Eagle 클래스는 Bird 클래스를 상속받았지만 fly메서드를 오버라이딩하여 구현하지 않았다.
# eagle 객체의 fly 메서드를 수행하는 순간 Bird 클래스의 fly 메서드가 수행되어
# NotImplementedError가 발생한다.

# 상속받는 클래스에서 메서드를 재구현하는 것을 메서드 오버라이딩이라고 한다.

# >> 오류 처리
class Eagle(Bird):
  def fly(self):
    print("very fast")

eagle = Eagle()
eagle.fly()

#! 예외 만들기

# 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다.
# 예외는 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.

class MyError(Exception):
  pass

# 별명을 출력하는 함수

def say_nick(nick):
  if nick == '바보':
    raise MyError()
  print(nick)

try:
  say_nick("천사")
  say_nick("바보")
except MyError:
  print("허용되지 않는 별명입니다.")

# 오류 메시지 사용

class MyError(Exception):
  def __str__(self):
    return "허용되지 않는 별명입니다."

try:
  say_nick("천사")
  say_nick("바보")
except MyError as e:
  print(e)

# __str__ 메서드는 print(e)처럼 오류메시지를 print문으로 출력할 경우에 호출되는 메서드이다.