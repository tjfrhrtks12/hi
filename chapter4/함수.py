#함수는 반복시청

def add(a,b):
    return a+ b
print(add(1,2))


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3,4,5))
#>>>15
#1,2,3,4,5를 모두 더한다.

def add_mul(choice, *args): 
     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
         result = 1 
         for i in args: 
             result = result * i 
     return result 
result = add_mul("add", 1,2,3,4)
print(result)
#>>>10    "add"의 입력값으로 1,2,3,4를 모두 더해서 10이 나온다.
result = add_mul("mul", 1,2,3,4)
print(result)
#>>>24     "mul"의 입력값으로 1,2,3,4를 모두 곱해서 24가 나온다.

#키워드 매개변수  (**)
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1,b=2)
#>>>{'a': 1, 'b': 2}
#딕셔너리로 출력된다.

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)
say_nick("맛스타님")
say_nick("조코딩님")
say_nick("바보")
#>>>나의 별명은 맛스타님 입니다.
#   나의 별명은 조코딩님 입니다.
#바보에서 리턴을 받아서 바보는 입력이 안된다.

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("이빠진퍄노", 20, False)
#>>>나의 이름은 이빠진퍄노 입니다.
#   나이는 20살입니다.
#   여자입니다.

###인풋#######
a = input()
print("유저가 입력한 것:" + a)
#터미널에 안녕이라고 입력하면
#유저가 입력한 것:안녕  이 출력됨

number = input("숫자를 입력하세요: ")
print(number)
#터미널에 2를 입력하면
#숫자를 입력하세요: 2
#2                      가 출렴됨

#인풋은 모든 것을 문자열로 취급한다.
  