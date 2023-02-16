### 딕셔너리 자료형

# 딕셔너리 : 대응 관계를 나타낼 수 있는 자료형 // 대응 관계를 나타내는 자료형들 : 배열, 해시
## 딕셔너리는 Key를 통해 Value를 얻는다.

### 딕셔너리 형태
# {Key1 : Value1, Key2:Value2, Key3:Value3}

dic = {'name':'lsa', 'phone':'010-1234-5678', 'birth':'0314'}

a = {1: 'hi'}

a = { 'a': [1,2,3]}

### 딕셔너리 쌍 추가, 삭제하기

a = {1: 'a'}

a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1,2,3]
print(a)

del a[1]
print(a)

### 딕셔너리에서 Key 사용해 Value 얻기

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

# 딕셔너리에서 요솟값을 얻는 방법 : 딕셔너리변수이름[key]
# 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없다.
# 튜플, 문자열은 요솟값을 얻고자 할 때 인덱싱이나 슬라이싱 기법 중 하나를 사용했다.
a = {1: 'a', 2: 'b'}
print(a[1]) # 딕셔너리 변수에서 [] 안의 숫자 1은 두 번째 요소를 뜻하는 것이 아니라 Key에 해당하는 1을 나타낸다.
print(a[2])

dic = {'name':'lsa', 'phone':'010-1234-5678', 'birth':'0314'}
print(dic['name'])
print(dic['birth'])
print(dic['phone'])

### 딕셔너리 주의사항
# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
# 동일한 Key가 2개 존재할 경우 1:'a'쌍이 무시된다.
a = {1: 'a', 1: 'b'}
print(a)

# Key에 리스트는 쓸 수 없다. // 튜플은 Key로 쓸 수 있다. (Key가 mutable값인지 immutable값인지에 달려 있다.)
# >> 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.
# 단, Value에는 변하는 값이든 변하지 않는 값이든 상관없이 아무 값이나 넣을 수 있다.

# a={[1,2] :'hi'} >> 오류 : 리스트를 키 값으로 사용할 수 없다.

### 딕셔너리 관련 함수들 

### Key 리스트 만들기(keys) ###

a={'name': 'lsa', 'phone': '010-1234-5678', 'birth': '0314'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])
# a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 리턴한다. 
# 리턴 값으로 리스트가 필요한 경우 : list(a.keys())를 사용하면 된다.
# 리스트로 변환하지 않아도 반복문에서 사용가능하다

for k in a.keys():
  print(k) # print(k) 입력 시 들여쓰기를 하지 않으면 오류가 발생한다.
# name
# phone
# birth >> 결괏값

print(list(a.keys()))
# ['name', 'phone', 'birth'] >> 결괏값 : dict_keys 객체를 리스트로 변환하는 방법이다.

### Value 리스트 만들기(values) ###

print(a.values()) # dict_values(['lsa', '010-1234-5678', '0314']) >> 결괏값 : Values만 얻는 방법이다.

### Key, Value 쌍 얻기 (items) ###

print(a.items()) # dict_items([('name', 'lsa'), ('phone', '010-1234-5678'), ('birth', '0314')]) >> 결괏값

### Key : Value 쌍 모두 지우기 (clear)

a.clear()
print(a) # {} >> 결괏값 // 빈 리스트 [], 빈 튜플 (), 빈 딕셔너리 {}

### Key로 Value얻기 (get) ###

a={'name': 'lsa', 'phone': '010-1234-5678', 'birth': '0314'}
print(a.get('name')) # lsa >> 결괏값
print(a.get('phone')) # 010-1234-5678 >> 결괏값

# get(x) 함수는 x라는 Key에 대응되는 Value를 리턴한다. 
# a.get('name')은 a['name']과 결괏(리턴)값이 동일하다. 
# 차이 a['nokey'] : Key오류발생, a.get('nokey') : None리턴

# get(x, '디폴트 값') : 딕셔너리 안에 찾으려는 Key가 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때 
print(a.get('nokey', 'foo')) # foo >> 결괏값

### 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)

a={'name': 'lsa', 'phone': '010-1234-5678', 'birth': '0314'}
print('name' in a) # True >> 결괏값
print('email' in a) # False >> 결괏값



