### 정규 표현식 ###

# 복잡한 문자열을 처리할 때 사용하는 기법
# 파이썬의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다.

# 정규식

# 정규식 사용X

data = """
  park 800905-1049118
  kim 700905-1059119
"""

result = []
for line in data.split("\n"):
  word_result = []
  for word in line.split(" "):
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
      word = word[:6] + "-" + "*******"
    word_result.append(word)
  result.append(" ".join(word_result))
print("\n".join(result))

# 정규식 사용

import re
data = """
  park 800905-1049118
  kim 700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))




