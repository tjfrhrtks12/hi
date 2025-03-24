#문장을 반복해서 수행해야 하 ㄹ경우 while 문을 사용한다. 그래서
# while 문을 '반복문'이라고도 부른다.

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit +1     #treeHit += 1  이라고 해도 똑같다.
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")
# >>>나무를 1번 찍었습니다.
#   나무를 2번 찍었습니다.
#   나무를 3번 찍었습니다.
#   나무를 4번 찍었습니다.
#   나무를 5번 찍었습니다.
#   나무를 6번 찍었습니다.
#   나무를 7번 찍었습니다.
#   나무를 8번 찍었습니다.
#   나무를 9번 찍었습니다.
#   나무를 10번 찍었습니다.
#   나무 넘어갑니다.

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number: """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())
##터미널에서 4를 입력할때까지 반복된다.

##다음 예는 커피 자판기 이야기를 파이썬 프로그램으로 표현해 본 것이다.
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break     #break를 안써주면 무한반복이 된다.성주피셜
#                   #Ctrl+C를 누르면 while문을 빠져나간다

##커피를 주냐, 거스름돈을 주냐, 다 떨어졌냐의 반복문
# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break
