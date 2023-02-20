### 다른 파일에서 모듈 불러오기 ###

import mod2
result = mod2.add(3, 4)
print(result) # 7 >> 결괏값

# 다른 파이썬 파일에서도 import mod2로 mod2 모듈을 불러와서 사용할 수 있다.
# 대화형 인터프리터에서 한 것과 마찬가지 방법이다.

# 위 예제가 정상적으로 실행되기 위해서는 modtest.py 파일과 mod2.py 파일이 동일한
# 디렉터리 (C:\vscPython\Ch05)에 있어야 한다.

### 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법

# mkdir mymod >> 폴더 생성
# move mod2.py mymod >> mod2파일 mymod폴더로 이동

# cmd 에서 python >> 파이썬 셸 실행
# >>> import sys : sys 모듈 불러오기
# 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈


# sys.path(리스트) : 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.
# sys.path에 C:\vscPython\mymod 디렉터리를 추가하면 아무 곳에서나 불러 사용할 수 있다.

# sys.path.append("C:/vscPython/Ch05/mymod")
# >> 디렉터리 추가 >> / 사용

# import mod2 
# print(mod2.add(3,4))
# 7 >> 결괏값

### PYTHONPATH 환경 변수 사용하기 ###
# 모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.

# C:\vscPython\Ch05> set PYTHONPATH=C:\vscPython\mymod
# C:\vscPython\Ch95> python
# >>> import mod2
# >>> print(mod2.add(3,4))
# 7 > 결괏값

# set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\vscPython\Ch05\mymod 
# 디렉터리를 설정한다. > 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용 할 수 있다.

