### 유니코드 ###

# 인코딩

# >>> a = "Life is too short"
# >>> b = a.encode('utf-8')

# >>> b
# b'Life is too short'

# >>> type(b)
# <class 'bytes'>

# 디코딩

# >>> b.decode('utf-8')
# 'Life is too short'

### 입출력과 인코딩 ###

# 파일을 읽거나 네트워크를 통해 데이터를 주고받을 때 추천하는 방법

# 1. 입력으로 받은 바이트 문자열은 가능한 한 가장 빨리 유니코드 문자열로 디코딩 할 것
# 2. 유니코드 문자열만 함수나 클래스 등에서 사용할 것
# 3. 입력에 대한 결과를 전송하는 마지막 부분에서만 유니코드 문자열을 바이트 문자열로 인코딩해서 반환할 것

# -*-coding:utf-8-*-
# 소스 코드 가장 위에 파일을 utf-8 인코딩으로 저장하기 위해 작성해야한다.