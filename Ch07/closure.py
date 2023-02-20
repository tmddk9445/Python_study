### 클로저

# 함수 안에 내부 함수(inner function)를 구현하고 그 내부 함수를 리턴하는 함수를 말한다.
# 외부 함수는 자신이 가진 변숫값 등을 내부 함수에 전달할 수 이싿.

# 어떤 수에 항상 3을 곱해 리턴하는 함수
def mul3(n):
  return n*3

class Mul:
  def __init__(self, m):
    self.m = m
  
  # def mul(self, n):
  #   return self.m * n

  def __call__(self, n): 
    return self.m * n
  # 함수 이름을 __call__로 바꾸었다.
  # Mul클래스로 만든 객체에 인수를 전달하여 바로 호출할 수 있도록 하는 메서드
  # mul3 객체를 mul3(10)처럼 호출할 수 있다.

if __name__ == "__main__":
  mul3 = Mul(3)
  mul5 = Mul(5)

  # print(mul3.mul(10))
  # print(mul5.nul(10))
  print(mul3(10))
  print(mul5(10))

def mul(m):
  def wrapper(n):
    return m * n
  return wrapper

if __name__ == "__main__":
  mul3 = mul(3)
  mul5 = mul(5)

  print(mul3(10))
  print(mul5(10))

# 외부 함수 (mul()) 안에 내부 함수 (wrapper())를 구현하였다. 
# 외부 함수는 내부 함수 wrapper()를 리턴한다.
# 파이썬은 함수가 함수를 리턴할 수 있다.

# mul() 함수에서 wrapper() 함수를 리턴할 때 mul() 함수 호출 시 
# 인수로 받은 m 값을 wrapper() 함수에 저장하여 리턴한다.
# >> 클래스가 특정한 값을 설정하여 객체를 만드는 과정과 매우 비슷하다.
# mul() 과 같은 함수를 클로저(Closure)라 한다.
