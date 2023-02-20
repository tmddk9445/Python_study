def echo_test():
  print("echo")

  # 다음 예제를 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 명력 프롬프트 창에서
  # set 명령어로 PYTHONPATH 환경 변수에 C:/vscPython/Ch05_package 디렉터리를 추가한다.
  # 그리고 파이썬 인터프리터(쉘)를 실행한다.

  # 아래의 실습은 cmd python 인터프리터에서 실행해야한다 (vsc X)

# 패키지 안의 함수를 실행하는 방법 

# 다음 예제는 import 예제이므로 하나의 예제를 실행하고 나서 다음 예제를 실행할 때에는
# 반드시 인터프리터를 종료하고 다시 실행해야 한다.

# 1. echo 모듈을 import하여 실행하는 방법
# echo 모듈은 ehco.py 파일이다.

# >>> import game.sound.echo
# game.sound.echo.ehco_test()
# echo

# 2. echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법

# >>> from game.sound import echo
# >>> echo.echo_test()
# echo

# 3. echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법

# >>> from game.sound.echo import echo_test
# >>> echo_test()
# echo

# 단, import game
# game.sound.echo.echo_test() 실행 불가 
# >> import game을 수행하면 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.

# import game.sound.echo.echo_test 실행 불가( echo_test 사용하는 것은 불가능하다. )
# >> 도트연산자를 사용해서 import a.b.c 처럼 import할 때 가장 마지막 항목인 c는 반드시
# 모듈 또는 패키지여야만 한다.