### while문 ###

# 반복해서 문장을 수행해야 할 경우
# 조건문이 참인 동안에 while문에 속한 문장들이 반복해서 수행된다.

treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1 # treeHit += 1 과 같다.
    print("나무를 %d번 찍었습니다." %treeHit) # %d !!
    if treeHit == 10 :
        print("나무 넘어갑니다.")

# 나무를 1번 찍었습니다.
# 나무를 2번 찍었습니다.
# 나무를 3번 찍었습니다.
# 나무를 4번 찍었습니다.
# 나무를 5번 찍었습니다.
# 나무를 6번 찍었습니다.
# 나무를 7번 찍었습니다.
# 나무를 8번 찍었습니다.
# 나무를 9번 찍었습니다.
# 나무를 10번 찍었습니다.
# 나무 넘어갑니다. >> 결괏값

# 여러 가지 선택지 중 하나를 선택해서 입력받는 예제
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number: """ # prompt : 여러 줄짜리 문자열


number = 0 
# 변수를 먼저 설정해 놓지 않으면 while문의 조건문인 number != 4에서 변수가 존재하지 않는다는 오류가 발생한다.
while number != 4:
    print(prompt)
    number = int(input()) # 사용자의 숫자 입력을 받아들이는 함수

### while문 강제로 빠져나가기 ###

coffee = 10
money = 300
while money :
    print("커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 커피를 줍니다.
# 남은 커피의 양은 9개입니다.
# 커피를 줍니다.
# ...
# 커피를 줍니다.
# 남은 커피의 양은 1개입니다.
# 커피를 줍니다.
# 남은 커피의 양은 0개입니다.
# 커피가 다 떨어졌습니다. 판매를 중지합니다.

coffee = 3

while True :
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money -300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

### while문의 맨 처음으로 돌아가기 ###

# 1부터 10까지의 숫자 중에서 홀수만 출력하는 것을
# while 문을 사용해서 작성해보자

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue # while문의 맨 처음(조건문)으로 돌아가기
    print(a)

# 1
# 3
# 5
# 7
# 9

### 무한루프 ###

# 무한루프(Loop) : 무한히 반복한다 >> while문으로 구현할 수 있다.
while True :
    print("Ctrl + c를 눌러야 while문을 빠져나갈 수 있습니다.")

