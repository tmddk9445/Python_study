### 데코레이터

#! 데코레이터 decorator

# 함수의 실행 시간을 측정할 때 ( 함수가 시작하는 순간의 시간 - 함수가 종료되는 순간의 시간 차이)

import time

def myfunc():
  start = time.time()
  print("함수가 실행됩니다.")
  end = time.time()
  print("함수 수행시간 : %f 초" % (end-start))

myfunc()

# 함수가 실행됩니다.
# 함수 수행시간 : 0.001000 초 >> 결괏값

import time

def elapsed(original_func): 
  # 함수를 인수로 받는다. // 파이썬은 함수도 객체이므로 함수 자체를 인수로 전달 할 수 있다.
  def wrapper():
    start = time.time()
    result = original_func()
    end = time.time()
    print("함수 수행시간 : %f 초" %(end-start))
    return result
  return wrapper

def myfunc():
  print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc) 
# 실제로는 elapsed() 내부의 wrapper() 함수가 실행되고 
# 이 함수는 전달받은 myfunc()함수를 실행하고 실행시간도 함께 출력한다
decorated_myfunc()

# 함수가 실행됩니다.
# 함수 수행시간 : 0.000999 초 >> 결괏값

# 데코레이터는 다음처럼 @를 이용한 어노테이션으로 사용할 수도 있다.

# import time

# def elapsed(original_func):
#   def wrapper():
#     start = time.time()
#     result = original_func()
#     end = time.time()
#     print("함수 수행시간 : %f 초" %(end - start))
#     return result
#   return wrapper

# @elapsed # @ + 데코레이터 함수명 이라는 어노테이션을 추가했다.
# def myfunc():
#   print("함수가 실행됩니다.")

# @elapsed
# def myfunc(msg):
#   print("'%s'을 출력합니다." %msg)

# # decorated_myfunc = elapsed(myfunc)
# # decorated_myfunc()

# # myfunc()
# myfunc("You need python") # 출력할 메시지를 myfunc 파라미터로 전달한다.

# >> 오류 : myfunc() 함수는 입력 인수가 필요하나 elapsed() 함수 내의 wrapper() 함수는
# 전달받은 myfunc() 함수를 입력 인수 없이 호출하기 때문이다.

# 데코레이터 함수는 기존 함수의 입력 인수에 상관없이 동작하도록 해야 한다.
# 데코레이터가 기존 함수가 어떤 입력 인수를 취할지 알 수 없기 때문이다.
# 전달 받아야 하는 기존 함수의 입력 인수를 알 수 없는 경우에는 
# *args 와 **kwargs 기법을 이용하여 해결해야 한다.

#? *args : 모든 입력 인수를 튜플로 변환하는 매개변수
#? **kwargs : 모든 키-값 형태의 입력 인수를 딕셔너리로 변환하는 매개변수이다.

import time

def elapsed(original_func): # 기존 함수를 인수로 받는다.
  def wrapper(*args, **kwargs): # *args, **kwargs 매개변수 추가
    start = time.time()
    result = original_func(*args, **kwargs) # 전달받은 *args, **kwargs를 입력파라미터로 기존함수 수행
    end = time.time()
    print("함수 수행시간 : %f 초" %(end - start)) # 수행시간을 출력한다.
    return result
  return wrapper

@elapsed
def myfunc(msg):
  """ 데코레이터 확인 함수 """
  print("'%s'을 출력합니다." %msg)

myfunc("You need python")