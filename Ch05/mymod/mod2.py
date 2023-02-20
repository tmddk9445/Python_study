### 클래스나 변수 등을 포함한 모듈 ###

PI = 3.141592

class Math:
  def solv(self, r):
    return PI * (r ** 2)

def add(a, b):
  return a+b

# 원의 넓이를 계산하는 Math클래스와 두 값을 더하는 add 함수 
# 원주율 값에 해당되는 PI 변수 >> 클래스, 함수, 변수 등을 모두 포함하고 있다.

# 대화형 인터프리터 실행
# cd 해당 모듈의 위치
# python

# >>> import mod2
# >>> print(mod2.PI)
# 3.141592

# a = mod2.Math()
# print(a.solv(2))
# 12.566368

# print(mod2.add(mod2.PI, 4.4))
# 7.541592000000005

