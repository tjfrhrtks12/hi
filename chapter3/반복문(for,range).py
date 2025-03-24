#하나씩 순차적으로 반복된다.  (for, in)
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# >>>one
#    two
#    three

#총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 
# 합격이고 그렇지 않으면 불합격이다. 
# 합격인지, 불합격인지 결과를 보여 주시오.
marks = [90, 25, 67, 45, 80]  #학생들의 시험 점수 리스트
number = 0   #학생에게 붙여 줄 번호
for mark in marks:    #90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
#>>>1번 학생은 합격입니다.
#   2번 학생은 불합격입니다.
#   3번 학생은 합격입니다.
#   4번 학생은 불합격입니다.
#   5번 학생은 합격입니다.

#앞에서 for 문 응용 예제를 그대로 사용해서 60점 이상인 사람에게는
#  축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도
#  전하지 않는 반복문     (for와 continue)
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)
#>>> 1번 학생 축하합니다. 합격입니다.
#    3번 학생 축하합니다. 합격입니다.
#    5번 학생 축하합니다. 합격입니다.

add = 0
for i in range(1, 11):
    add = add + i
print(add)
#>>>55
#1부터 10까지의 숫자들을 전부 더한다. 
for i in range(2,10):        # 1번 for문
     for j in range(1, 10):   # 2번 for문
         print(i*j, end=" ") 
     print('') 
# #>>>2 4 6 8 10 12 14 16 18
#     3 6 9 12 15 18 21 24 27
#     4 8 12 16 20 24 28 32 36
#     5 10 15 20 25 30 35 40 45
#     6 12 18 24 30 36 42 48 54
#     7 14 21 28 35 42 49 56 63
#     8 16 24 32 40 48 56 64 72
#     9 18 27 36 45 54 63 72 81 