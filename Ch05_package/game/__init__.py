### __init__.py의 용도

# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

# from game.sound import *
# echo.echo_test() >> 이름 오류

# 특정 디렉터리의 모듈을 *를 사용하여 import할 때에는 
# 디렉터리의 __init__.py 파일에 __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.

