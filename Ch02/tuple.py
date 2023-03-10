### 튜플 자료형

# 리스트와의 차이점 #
## 리스트는 []로 둘러싸지만 튜플은 ()으로 둘러싼다.
## 리스트는 요소 값의 생성, 삭제, 수정이 가능하지만 튜플은 요소 값을 바꿀 수 없다.
## 튜플 요솟값을 변경하거나 del 함수를 통해서 삭제하려 하면 오류가 뜬다.

### 튜플
t1=()
t2=(1,) # 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
t3=(1,2,3)
t4=1,2,3 # 괄호()를 생략해도 된다.
t5=('a', 'b', ('ab', 'cd'))

### 튜플 인덱싱

t1=(1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

### 튜플 슬라이싱

t1=(1, 2, 'a', 'b')
print(t1[1:])

### 튜플 더하기
t1=(1, 2, 'a', 'b')
t2=(3, 4)
t3=t1+t2
print(t3)

### 튜플 곱하기(반복)

t2=(3, 4)
t3=t2*3
print(t3)

### 튜플 길이 구하기
t1=(1, 2, 'a', 'b')
print(len(t1))

### 튜플은 요솟값을 변경할 수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.
