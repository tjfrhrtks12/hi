#‘돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어간다.’
money = True 
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")
#>>>택시를 타고 가라
#True가 아닌 False일 경우 "걸어가라"가 출력됨
#조건문 뒤에 (:)은 필수다!


# 비교연산자	설명
# x < y	    x가 y보다 작다.
# x > y 	x가 y보다 크다.
# x == y	x와 y가 같다.
# x != y	x와 y가 같지 않다.
# x >= y	x가 y보다 크거나 같다.
# x <= y	x가 y보다 작거나 같다.

#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 
# 그렇지 않으면 걸어가라.
money = 2000
if money >= 3000:
    print('택시를 타고 가라')
else:
    print("걸어가라")
#>>>걸어가라

# 연산자	설명
# x or y	x와 y 둘 중 하나만 참이어도 참이다.
# x and y	x와 y 모두 참이어야 참이다.
# not x	x가 거짓이면 참이다.

#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 
# 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
#>>>택시를 타고 가라

money = 2000
card = False
if money >=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
#>>>걸어가라


#   in	         not in
# x in 리스트	x not in 리스트
# x in 튜플	    x not in 튜플
# x in 문자열	x not in 문자열

print(1 in[1, 2, 3])
#>>>True
print(1 not in[1, 2, 3])
#>>>False

print('p' in 'python')    #p는 python에 포함되는가?
#>>>True
print('z'not in 'python')   #z는 python에 포함되어있지 않은가?
#>>>True

#만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
#>>>택시를 타고 가라

#주머니에 돈이 있으면 택시를 타고 가고, 
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 
# 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
#>>>택시를 타고 가라
#줄여서
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
#>>>택시를 타고 가라

