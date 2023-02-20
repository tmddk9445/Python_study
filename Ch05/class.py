### 클래스 ###

result = 0

def add(num):
  global result
  result += num
  return result

print(add(3))
print(add(4))

class Calculator:
  def __init__ (self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

cal1 = Calculator() # 객체
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.add(3))
print(cal1.add(7))

# 3
# 7
# 10
# 17 >> 결괏값

class Calculator:
  def __init__ (self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

  def sub(self, num):
    self.result -= num
    return self.result

class Cookie:
  pass

a = Cookie()
b = Cookie() 
# a, b가 객체이다.
# a 객체는 Cookie의 인스턴스이다.
# 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.

# a 객체
# a는 Cookie의 인스턴스

#component 사칙연산 클래스 만들기

class FourCal:
  def setdata(self, first, second): # 메서드
    self.first = first
    self.second = second

a = FourCal()
type(a)

a.setdata(4,2) 
# setdata 메서드의 첫 번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달된다.
# self값에는 a.setdata(4,2)에서 a가 전달된다.
# print(a.add())

# 클래스를 통해 메서드 호출
a = FourCal()
FourCal.setdata(a,4,2)
# 객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야한다.
a = FourCal()
a.setdata(4,2)

# 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.

print(a.first) # 4
print(a.second) # 2 >> 결괏값

# a 객체에 객체변수 first, second가 생성되었음을 확인할 수 있다.

a = FourCal()
b = FourCal()

a.setdata(4,2)
print(a.first)

b.setdata(3,7)
print(b.first) # 3 >> 결괏값

print(a.first) # 4 >> 결괏값

# a 객체의 first값은 b 객체의 first값에 영향받지 않고 원래 값을 유지하고 있다.
# >> 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.


class FourCal:
  def setdata(self, first, second):
    self.first = first
    self.second = second

  def add(self):
    result = self.first + self.second
    return result

a = FourCal()
a.setdata(4,2)

print(a.add()) # 6 >> 결괏값
# a 객체에 의해 add 메서드가 수행되면 
# add 메서드의 self에는 객체 a가 자동으로 입력된다.

print('##########')

class FourCal2:
  def setdata(self, first, second):
    self.first = first
    self.second = second

  def add(self):
    result = self.first + self.second
    return result
  
  def mul(self):
    result = self.first * self.second
    return result
  
  def sub(self):
    result = self.first - self.second
    return result

  def div(self):
    result = self.first / self.second
    return result

a = FourCal2()
b = FourCal2()

a.setdata(4,2)
b.setdata(3,8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

#component 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드

# a = FourCal2()
# a.add()

# 파이썬 메서드 이름으로 __init__을 사용하면
# 그 메서드는 생성자가 된다.

class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
    # __init__으로 메서드이름을 지정하는 경우
    # 생성자로 인식되어 객체가 생성되는 시점에
    # 자동으로 호출되는 차이가 있다.
  
  def setdata(self, first, second):
    self.first = first
    self.second = second
  
  def add(self):
    result = self.first + self.second
    return result
  
  def sub(self):
    result = self.first - self.second
    return result
  
  def mul(self):
    result = self.first * self.second
    return result

  def div(self):
    result = self.first / self.second
    return result

a = FourCal(4,2)
print(a.first)
print(a.second)

print(a.add())
print(a.div())

#component 클래스의 상속

class MoreFourCal(FourCal): 
  # class 클래스 이름(상속할 클래스 이름)
  def pow(self):
    result = self.first ** self.second
    return result

a = MoreFourCal(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(a.pow())
print(a.add())

#component 메서드 오버라이딩

# a = FourCal(4,0)
# a.div() >> ZeroDivisionError 오류

class SafeFourCal(FourCal):
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second
# 메서드 오버라이딩 : 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것

# 메서드 오버라이딩을 하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

a = SafeFourCal(4,0)
print(a.div())

#component 클래스 변수

class Family:
  lastname = "김" 
  # 클래스 변수 : 클래스 안에 변수를 선언하여 생성한다.

print(Family.lastname)
# 클래스이름.클래스 변수로 사용할 수 있다.

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

# 클래스 변수와 동일한 이름의 객체 변수를 생성하면

a.lastname = "최"
print(a.lastname)
# a객체에 lastname이라는 객체변수가 새롭게 생성
# 객체변수는 클래스 변수와 동일한 이름으로 생성할 수 있다.

print(Family.lastname) # 객체변수에 영향을 받지 않는다.
print(b.lastname)












