### 모듈 ###

# def add(a,b):
#   return a + b
# def sub(a,b):
#   return a - b >> 아래에 다시 작성

### 모듈 사용법

# cd C:\파일이름(모듈이 있는 파일)
# > dir
# > python : 대화형 인터프리터로 이동

# >>> import 모듈이름(모듈파일이름)
# == from 모듈이름 import 모듈함수
# from 모듈이름 import 모듈함수1, 모듈함수2
# from 모듈이름 import * (모든 것)

# >>> print(mod1.add(3,4)) : 모듈이름.함수이름
# == print(add(3,4)) : 함수이름 (add 함수만 사용가능)

# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다.

#component if __name__ "__main__"

# if __name__ == "__main__":
#   # python 모듈.py 처럼 직접 이 파일을 실행했을 때
#   # __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.

#   # 반대로 대화형 인터프리터나 다른 파일에서 
#   # 이 모듈을 불러서 사용할 때는는 거짓이 되어
#   # if문 다음 문장이 수행되지 않다.

# def add(a, b):
#   return a+b

# def sub(a, b):
#   return a-b

# print(add(1,4))
# print(sub(4,2)) >> 아래에 다시 작성

# C:\vscPython\Ch05> python mod1.py
# 5
# 2 >> 결괏값

# mod1.py 파일의 add와 sub 함수를 사용하기 위해
# mod1 모듈을 import할 때는 import를 수행하는 순간 해당 파일이 실행되어
# 결괏값을 출력한다. (함수만 사용할 수 X)

# __name__ 변수

def add(a, b):
  return a+b
def sub(a, b):
  return a-b

if __name__ == "__main__":
  print(add(1,4))
  print(sub(4,2))
경우fl
# __name__ 변수를 사용하는 경우fl
# C:\vscPython\Ch05 > python mod1.py처럼 직접 이 파일을 실행할 경우
# __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.
# __name__ 변수에는 __main__ 값이 저장된다.

# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는
# __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
# __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

# >>> import mod1
# >>> mod1.__name__
# 'mod1'


