__all__ = ['echo']

# >> 특정 디렉터리의 모듈을 *를 사용하여 import할 때에는 다음과 같이 해당 디렉터리의
# __init__.py 파일에 __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.

# __all__
# >> sound 디렉터리에서 * 기호를 사용하여 import할 경우 이곳에 정의된 echo 모듈만 import된다는 의미이다.

### from game.sound.echo import * 는 __all__ 과 상관없이 무조건 import된다.
# __all__과 상관없이 무조건 import 되는 경우는 
# from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우이다.

# >>> from game.sound import *
# >>> echo.echo_test()
# echo 

