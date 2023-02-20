### 패키지 ###

# 패키지는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
# 모듈 이름 A.B // A : 패키지 이름 B : 패키지의 B모듈

# 파이썬에서 모듈은 하나의 .py 파일이다.

# 파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어진다.

# 가상의 game 패키지 예

# game/
#   __init__.py
#   sound/
#     __init__.py
#     echo.py
#     wav.py
#   graphic/
#     __init__.py
#     screnn.py
#     render.py
#   play/
#     __init__.py
#     run.py
#     test.py

### game, sound, grapic, play는 디렉터리이고 확장자가 .py인 파일은 파이썬 모듈이다.
# game 디렉터리가 이 패키지의 루트 디렉터리이고 sound, graphic, play는 서브 디렉터리이다.

#component 패키지 만들기

# 폴더 생성 : mkdir 폴더이름
# 

