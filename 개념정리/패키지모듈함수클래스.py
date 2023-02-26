
#! 1. 패키지 (package = 라이브러리 library)

# 특정 기능과 관련된 여러 모듈을 한 그룹으로 묶은 것
# 패키지 안에 패키지가 있을 수도 있다.
# import 모듈 from 패키지 (import 패키지 가능)

#! 2. 모듈 (module)

# 여러 기능들이 뭉쳐진 하나의 .py 파일
# 함수, 클래스, 변수 등 포함
# import 모듈

#! 3. 함수 (function)

# 하나의 기능을 가진 코드의 집합
# 함수를 사용한다. = 함수를 호출한다.
# 함수 사용 형태 : 함수()
#   필요한 경우 ()안에 매개변수 또는 옵션
# 종류 : 내장함수(built in), 외장함수(import 필요)

# 클래스 안에 구현된 함수를 메서드라고 부른다.

#? 패키지 = 카테고리 (Python)
#? 모듈 = 카테고리 내 게시물 ([ptyhon] 패키지 모듈, 함수, 클래스 개념 정리)
#? 함수 = 위의 게시물 내 여러 개념들 (패키지, 모듈, 함수, 클래스)

#! 클래스

# 파이썬은 객체 지향 언어로 클래스 기반으로 객체(인스턴스)를 만들어서 사용한다.
# 한 파이썬 파일(.py) 내에서 "class class명(): "을 통해 클래스 선언

# >> 패키지/라이브러리 안에
# >> 모듈 A B C D
# >> 모듈 안에 함수 A B C
# >> 모듈 안에 클래스 A B

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

# PyQt5.QtWidgets : 패키지.모듈
# QApplication, QWidget, QLabel : 클래스

# class MyApp(QWidget): # 현재 모듈 안에서 새로운 클래스 선언
#     def __init__(self):
#         super().__init__()
#         MyApp.label_date = QLabel(); # 클래스
#         self.initUI()
        
#         def initUI(self):

#! 객체와 인스턴스의 차이

# 클래스로 만든 객체 : 인스턴스

# 객체와 인스턴스의 차이
# a = Cookie() 이렇게 만든 a는 객체이다.
# a 객체는 Cookie의 인스턴스이다. 

# 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용

# "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 
# "a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.
