### 제너레이터 ###

#! 제너레이터 

# 함수가 연속된 값을 차례대로 리턴할 경우 (하나의 값만 리턴X)

# 이터레이터와 마찬가지로 next() 함수 호출 시 그 값을 차례대로 얻을 수 있다.
# 결과 리턴 시 return 대신 yield 키워드를 사용한다.

def mygen():
  yield 'a'
  yield 'b'
  yield 'c'

g = mygen() 

type(g) # <class 'generator'> >> 결괏값

next(g) # 'a'
next(g) # 'b'
next(g) # 'c' 
# >> 제너레이터는 yield라는 문장을 만나면 그 값을 리턴하되 현재 상태를 그대로 기억한다.
# >> 일시 정지

# next(g)
# StopIteration >> 더는 리턴할 값이 없다면 StopIteration 예외가 발생한다.

#? 제너레이터 표현식

def mygen():
  for i in range(1, 1000):
    result = i * i
    yield result
gen = mygen()

print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9 >> 3번 호출 했으로 3의 제곱 9가 출력된다.

gen = (i * i for i in range(1, 1000)) 
# 튜플 표현식
# mygen() 함수로 만든 제너레이터와 완전히 똑같이 기능한다.
# 리스트 컴프리헨션 구문과 비슷하다
# 다만, 리스트 대신 튜플을 이용하였다.
# 제너레이터 표현식이라고 부른다.

#? 제너레이터와 이터레이터

# 클래스를 이용하여 이터레이터를 작성하면 복잡한 행동을 하게 할 수 있다.
# 제너레이터 표현식 등을 이용하면 간단하게 이터레이터를 만들 수 있다.

# 이터레이터의 성격에 따라 클래스로 만들 것인지 제너레이터로 만들 것인지 선택해야 한다.

# (i * i for i in range(1, 1000)) 제너레이터를 이터레이터 클래스로 구현

class MyItertor:
  def __iter__(self):
    self.data = 1
  
  def __iter__(self):
    return self
  
  def __next__(self):
    result = self.data * self.data
    self.data += 1
    if self.data >= 1000:
      raise StopIteration
    return result

#? 제너레이터의 쓰임새

import time

def longtime_job():
  print("job start")
  time.sleep(1)
  return "done"

list_job = iter([longtime_job() for i in range(5)])
print(next(list_job))

# longtime_job()이라는 함수는 총 실행 시간이 1초인 함수이다. 
# longtime_job() 함수를 5번 실행하여 리스트에 그 결괏값을 담고 이를 이터레이터로 변경한 후 
# 그 첫 번째 결괏값을 호출하는 예제이다.

# job start
# job start
# job start
# job start
# job start
# done >> 결괏값 : 리스트를 만들 때 이미 5개의 함수를 모두 실행하므로 5초의 시간이 소요된다.

import time

def longtime_job():
  print("job start")
  time.sleep(1)
  return "done"

# list_job = iter([longtime_job() for i in range(5)]) 코드를
list_job = (longtime_job() for i in range(5)) # 제너레이터 표현식으로 변경
print(next(list_job))

# job start
# done >> 결괏값 : 모든 함수를 한꺼번에 실행하는 것이 아니라 필요할 때만 실행하는 방식으로 바뀐다.
# 시간이 오래 걸리는 작업을 한꺼번에 처리하기 보다는 필요한 경우에만 순차적으로 사용할 때
# 제너레이터를 유용하게 사용할 수 있다.

