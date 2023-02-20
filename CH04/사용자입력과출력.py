### 사용자의 입력과 출력 ###

#component input의 사용

a = input()
print(a) # Life is too short, you need python >> 입력값, 결괏값

# input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.

#component 프롬프트를 띄워서 사용자 입력받기

# 사용자에게 입력받을 때 안내 문구 또는 질문이 나오도록 하고 싶을 때가 있다.
# input()의 괄호 안에 안내문구를 입력하여 프롬프트를 띄워주면 된다.

number = input("숫자를 입력하세요 : ")
print(number) # 입력받은 number은 숫자가 아닌 문자열이다.

#component print 자세히 알기

# 데이터를 출력하는 print문

a=123
print(a)
a="python"
print(a)
a=[1,2,3]
print(a)

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다.
print("Life""is""too short")
print("Life"+"is"+"too short") # 결괏값이 동일하다.

# 한 줄에 결괏값 출력하기
for i in range(10):
  print(i, end= '') # 0123456789 >> 결괏값 // end 매개변수의 초깃값은 줄바꿈(\n) 문자이다.