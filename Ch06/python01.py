### 파이썬 프로그램 ###

# 구구단 프로그램

# 함수 이름 : gugudan
# 입력받는 값 : 2
# 출력하는 값 : 2,4,6,...,18
# 결과를 어떤 형태로 저장할 것인가 : 리스트(연속된 자료형)

# def gugudan(n):
#   print(n)

# gugudan(2) # 2 >> 결괏값

def gugudan(n):
  result = []
  result.append(n*1)
  result.append(n*2)
  result.append(n*3)
  result.append(n*4)
  result.append(n*5)
  result.append(n*6)
  result.append(n*7)
  result.append(n*8)
  result.append(n*9)
  return result

print(gugudan(2)) # [2, 4, 6, 8, 10, 12, 14, 16, 18] >> 결괏값

def gugudan(n):
  result = []
  i = 1
  while i < 10:
    result.append(n * i)
    i = i + 1
  return result

print(gugudan(2)) # [2, 4, 6, 8, 10, 12, 14, 16, 18] >> 결괏값