# def render_test():
#   print("render") >> 아래에 다시 작성

### relative 패키지

# graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py모듈을 사용하고 싶을 경우

# from game.sound.echo import echo_test
# def render_test():
#   print("render")
#   echo_test()

# relative하게 import하는 방법

from ..sound.echo import echo_test 
# .. 은 render.py 파일의 부모 디렉터리를 의미한다.
# render.py 파일의 부모 디렉터리는 game이다. // 현재 디렉터리는 graphic

def render_test():
  print("render")
  echo_test()