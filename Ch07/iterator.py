### 이터레이터 ###

#! 이터레이터 

for a in [1,2,3]:
  print(a)

  # 리스트 [1,2,3]을 for문으로 차례대로 하나씩 출력하는 예제
  # > for문과 같은 반복 구문을 적용할 수 있는 리스트와 같은 객체를 반복 가능 (iterable) 객체라 한다.

#? 이터레이터란 

# 이터레이터는 next()함수 호출 시 그 다음 값을 리턴하는 객체이다.

# 리스트는 반복가능 객체이다. >> 리스트는 이터레이터일까?

# a = [1,2,3]
# next(a) # 'list' object is not an iterator >> 오류

# 반복 가능하다고 해서 이터레이터는 아니다!
# 하지만, 반복 가능하다면 iter() 함수를 이용하여 이터레이터로 만들 수 있다.

a = [1,2,3]
ia = iter(a)
type(ia) # <class 'list_iterator'> 이터레이터 타입이다.

next(ia) # 1 >> next() 함수 호출 시 이터레이터 객체의 요소를 차례대로 리턴한다.
next(ia) # 2
next(ia) # 3
# next(ia) 
# StopIteration >> 더는 리턴할 값이 없다면 StopIteration 예외가 발생한다.

# for문을 이요하여 이터레이터의 값 가져오기

a = [1,2,3]
ia = iter(a)
for i in ia:
  print(i)

# 1
# 2
# 3 
# >> for 문을 이용할 경우 next() 함수를 따로 호출할 필요도 없다 (for문이 자동으로 호출)
# StopIteration 예외에 신경 쓸 필요도 없다.

for i in ia:
  print(i) 
  # >> for문을 이용하여 반복하고 난 후에는 다시 반복하더라도 더는 그 값을 가져오지 못한다.
  # next()로 그 값을 한 번 읽으면 그 값을 다시는 읽을 수 없다.

#? 이터레이터 만들기

# iter() 함수를 이용하면 리스트를 이터레이터로 만들 수 있다.
# iter() 함수를 이용하지 말고 직접 이터레이터를 만드는 방법

# 이터레이터는 클래스에 __iter__와 __next__라는 두 개의 메서드를 구현하면 만들 수 있다.

class MyItertor: # class ReverseItertor
  def __init__(self, data): # 이터레이터 객체 생성 하고자 각가의 메서드를 구현
    self.data = data
    self.position = 0

  def __iter__(self): # 이터레이터 객체를 리턴하는 메서드
    return self # MyItertor 클래스에 의해 생성되는 객체를 의미하는 self를 리턴한다.
  
  def __next__(self): # next() 함수 호출 시 수행되므로 MyIterator 객체 생성 시 전달한 데이터를 하나씩 리턴
    if self.position >= len(self.data): # 더는 리턴 할 값이 없으면 StopIteration 예외를 발생시킨다.
      raise StopIteration
    result = self.data[self.position]
    self.position += 1
    return result

if __name__ == "__main__":
  i = MyItertor([1,2,3]) 
  # ReverseItertor([1,2,3]) >> 데이터를 역순으로 출력한다. 3,2,1
  for item in i:
    print(item)

# 1
# 2
# 3 >> 결괏값