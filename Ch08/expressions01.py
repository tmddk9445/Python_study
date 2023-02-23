### 정규 표현식 ###

# 복잡한 문자열을 처리할 때 사용하는 기법
# 파이썬의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다.

#! 메타문자 : 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자

# . ^ $ * ? {} [] \ | ()

#? 문자 클래스 []

# [] 사이의 문자들과 매치
# 문자 클래스를 만드는 메타 문자인 [] 사이에는 어떤 문자도 들어갈 수 있다.

# [abc] # 'a, b, c 중 한개의 문자와 매치'를 뜻한다.

# a는 정규식과 일치하는 문자인 a가 있으므로 매치
# before는 정규식과 일치하는 문자인 b가 있으므로 매치
# dude는 매치X

# [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From-To)를 의미한다.
# [a-c]라는 정규 표현식은 [abc]와 동일
# [0-5]라는 정규 표현식은 [012345]와 동일

# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자

# 문자클래스 ^ : 반대를 의미한다.(not)
# [^0-9] : 숫자가 아닌 문자만 매치된다.

# \d : 숫자
# \D : 숫자가 아닌 것
# \s : whitespace 문자와 매치 [\t\n\r\f\v]와 동일
# >> 맨 앞의 빈칸은 공백문자(space)를 의미한다.
# \w : 문자 + 숫자와 매치
# \W : 문자 + 숫자가 아닌 문자와 매치

#? Dot(.)

# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치
# re.DOTALL 옵션을 주면 \n 문자와도 매치된다.

# a.b : "a + 모든 문자 + b"
# a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치된다.

#aab 매치
#a0b 매치
#abc 매치X

# a[.]b : "a + Dot(.)문자 + b" // Dot문자 그대로!

#a.b 매치
#a0b 매치X

#? 반복 (*)

# ca*t : * 바로 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다.

# ct cat caaaaaaaat : 모두 매치

#? 반복 (+)

# + 는 최소 1번 이상 반복 될 때 사용한다.

# ca+t : "c + a(1번 이상 반복) + t"

# ct 매치X
# cat caaaat caaaaaat : 모두 매치


#? 반복 ({m,n}, ?)

# 반복 횟수 제한 {}

# {m,n}정규식을 사용하면 반복횟수가 m부터 n까지 매치할 수 있다.
# m 또는 n을 생략할 수도 있다.

# {3,}처럼 사용하면 반복 횟수가 3 이상인 경우
# {,3} 반복 횟수가 3 이하 의미

# 생략된 m은 0과 동일
# 생략된 n은 무한대(2억 개 미만)

# {1,} : + 와 동일
# {0,} : * 와 동일

# {m}
# ca{2}t : "c + a(반드시 2번 반복) + t"

# ca{2,5}t : "c + a(2~5회 반복) + t"
# cat 매치X
# caat caaaaat 매치

# ?
# {0,1}과 같다. (0~1회 반복)

# ab?c : "a + b(있어도 되고 없어도 된다.) + c"
# abc ac : 모두 매치

# *, +, ? 메타 문자를 사용하는 것이 좋다.

#! re 모듈

# 파이썬에서 정규 표현식을 지원하는 re모듈
# regular expression의 약어

# >>> import re
# >>> p = re.compile('ab*') 
# re.compile을 사용하여 정규 표현식을 컴파일한다.

# 패턴이란 정규식을 컴파일한 결과이다.

#! 정규식을 이용한 문자열 검색

# 컴파일된 패턴 객체를 사용하여 문자열 검색 수행

# match() : 문자열의 처음부터 정규식과 매치되는지 조사
# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
# finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴한다.

# match, search는 정규식과 매치될 때는 match 객체를 리턴하고
# 매치되지 않을 때는 None을 리턴한다.

# match객체란 정규식의 검색 결과로 리턴된 객체를 말한다.

# >>> import re
# >>> p = re.compile('[a-z]+')

#? match : 문자열의 처음부터 정규식과 매치

# >>> m = p.match("python")
# print(m)
# <re.Match object; span=(0, 6), match='python'> >> 결괏값

# "python" 문자열은 [a-z]+ 정규식에 부합되므로 match 객체를 돌려준다.

# >>> m = p.match("3 python")
# >>> print(m)
# None >> 결괏값

#? 정규 표현식 흐름

# p = re.compile(정규 표현식)
# m = p.match('string goes here')
# if m:
#   print('Match found : ', m.group())
# else:
#   print('No match')

# match의 결괏값이 있을 때만 그 다음 작업을 수행

#? search : 문자열 전체를 검색

# >>> m = p.search("python")
# >>> print(m)
# <re.Match object; span=(0, 6), match='python'>

# >>> m = p.search("3 python")
# >>> print(m)
# <re.Match object; span=(2, 8), match='python'>

# search는 문자열의 처음부터 검색X
# 문자열 전체를 검색 : 3 이후의 "python"문자열과 매치

#? findall : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴

# >>> result = p.findall("life is too short")
# >>> print(result)
# ['life', 'is', 'too', 'short'] >> 결괏값

#? finditer : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴

# findall과 동일하지만 그 결과로 반복 가능한 객체를 리턴한다.
# 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.

# >>> result = p.finditer("life is too short")
# >>> print(result)
# <callable_iterator object at 0x01F5E390>

# >>> for r in result : print(r)

# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

#! match/search 객체의 메서드

# match() : 문자열의 처음부터 정규식과 매치되는지 조사
# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.

# 정규식을 사용한 문자열 검색 수행
# > 어떤 문자열이 매치되었는가?
# > 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

# group() : 매치된 문자열을 리턴한다.
# start() : 매치된 문자열의 시작 위치를 리턴한다.
# >> match메서드에서 결괏값은 항상 0이다. (match메서드는 항상 문자열의 시작부터 조사한다.)
# end() : 매치된 문자열의 끝 위치를 리턴한다.
# span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.

# >>> m = p.match("python")
# >>> m.group()
# 'python'
# >>> m.start()
# 0
# >>> m.end()
# 6
# >>> m.span()
# (0, 6)

# >>> m = p.search("3 python")
# >>> m.group() // 문자열 리턴
# 'python'
# >>> m.start()
# 2
# >>> m.end()
# 8
# >>> m.span()
# (2, 8)

# 모듈 단위로 수행하기

# re.compile을 사용하여 컴파일된 패턴 객체 사용
# re 모듈

# >>> p = re.compile('[a-z]+')
# >>> m = p.match("python")

# 축약된 형태 : 컴파일과 match 메서드를 한 번에 수행할 수 있다.
# >>> m = re.match('[a-z]+', "python")

# 한 번 만든 패턴 객체를 여러번 사용해야 할 때는 이 방법 보다 
# re.compile을 사용하는 것이 편하다.

#! 컴파일 옵션

# 정규식을 컴파일할 때 사용하는 옵션

# DOTALL(S) : (.)이 줄바꿈 문자(\n)를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) : 대소문자에 관계없이 매치한다.
# MULTILINE(M) : 여러줄과 매치할 수 있도록 한다.
# >> ^, $ 메타문자의 사용과 관계가 있는 옵션이다.
# VERBOSE(X) : verbose모드를 사용할 수 있게 한다.
# >> 정규식을 보기 편하게 만들 수 있고 주석 등을 사용할 수 있게 된다.

# re.DOTALL 전체 옵션 이름 // re.S 약어사용

#? DOTALL(S) 

# >>> p = re.compile('a.b', re.DOTALL)
# >>> m = p.match('a\nb')
# >>> print(m)
# <re.Match object; span=(0, 3), match='a\nb'>

# 여러 줄로 이루어진 문자열에서 줄바꿈 문자에 상관없이
# 검색할 때 많이 사용한다.

#? IGNORECASE(I)

# >>> p = re.compile('[a-z]+', re.I)
# >>> p.match('python')
# <re.Match object; span=(0, 6), match='python'>
# >>> p.match('Python')
# <re.Match object; span=(0, 6), match='Python'>
# >>> p.match('PYTHON')
# <re.Match object; span=(0, 6), match='PYTHON'>

# [a-z]+ 정규식은 소문자만을 의미하지만
# re.I 옵션으로 대소문자 구별 없이 매치된다.

#? MULTILINE(M)

# ^, $와 연관된 옵션이다.
# ^ : 문자열의 처음을 의미한다.
# $ : 문자열의 마지막을 의미한다.

# ^python : 문자열의 처음은 항상 python으로 시작되어야 매치
# python$ : 문자열의 마지막은 항상 python으로 끝나야 매치


