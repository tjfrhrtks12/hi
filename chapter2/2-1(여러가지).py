#한꺼번에 주석처리 = ctrl + /

a = "20230331Rainy"
date = a[:8]          #0에서8전까지
weather = a[8:]       #8부터 끝까지
print(date)
print(weather)
#>>>20230331
#   Rainy

a = "I eat %d apples." % 15    
# %d에 15를 넣어준다
print(a)
#>>>I eat 15 apple.

a = "I eat %s apples." % "five"     
# %s s는 string [문자를 넣어준다],숫자도 가능하다
print(a)
#>>>I eat five apple.

number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)
#>>>I ate 10 apples. so I was sick for three days.
#숫자에 맞게 단어가 들어간다, 순서를 바꿀 수 있다
a = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)
#>>>I ate 10 apples. so I was sick for 3 days.
#이렇게도 사용 가능하다
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'         
print(a)
#>>>나의 이름은 홍길동입니다. 나이는 30입니다.

#f로 더 쉽게 활용할 수 있다.

y = 3.141592
a= f'{y:0.4f}'
print(a)
#>>>3.1416

#문자수 세주기
a= "hobby"
print(a.count('b'))
#>>>2

#위치 찾기(index)
a= "abcde"
print(a.find('b'))
#>>>1

#중간문자투입   (join)
a = "and".join('ABCD')
print(a)
#>>>AandBandCandD

# 소문자를 대문자로 바꾸기 - upper
# 대문자를 소문자로 바꾸기 - lower
# 오른쪽 공백 지우기 - rstrip\
# 양쪽 공백 지우기 - strip

#문자열 바꾸기 - replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))
#>>>Your leg is too short

#문자열 나누기 - split
a = "Life is too short"
print(a.split())
#>>>['Life', 'is', 'too', 'short']
#띄어쓰기를 기준으로 나눈다 다른 방법으로는
a = "a:b:c:d"
print(a.split(":"))
#>>>['a', 'b', 'c', 'd']
#:를 기준으로 나눈다

#리스트는 대괄호([])를 사용한ㄷ.
odd = [1, 3, 5, 7, 9]
print(type(odd))
#>>><class 'list'>
#리스트 안에 리스트
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])
#>>>['a', 'b', 'c']
#리스트 안에 리스트의 값  (대괄호 하나 더 추가)
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][1])
#>>>b
a = [1, "hello", 3, ['a', 'b', 'c']]
print(a[1][0])
#>>>h

#리스트 안의 값을 변경할때
a= [1, 2, 3]
a[2] = 4
print(a)
#>>>[1, 2, 4]

#리스트안의 값을 뺄때
a= [1, 2, 3]
del a[1]
print(a)
#>>>[1, 3]

#리스트 안의 값 추가
a = [1, 2, 3]
a.append(4)
print(a)
#>>>[1, 2, 3, 4]
#리스트 안의 리스트 추가
a = [1, 2, 3]
a.append([5, 6])
print(a)
#>>>[1, 2, 3, [5, 6]]

#리스트 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)
#>>>[1, 2, 3, 4]
#거꾸로 
a.sort()
[2, 3, 4 ,1]
#역순
a.sort()
a.sort()
[4, 3, 2, 1]

#몇번째에 값을 추가하겠다.(insert)
a = [1, 2, 3]
a.insert(1,4)
print(a)
#>>>[1, 4, 2, 3]

#값을 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
#>>>[1, 2, 1, 2, 3]
#뒤의 값도 삭제하고 싶을경우    remove를 연속 두번해준다.
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a.remove(3)
print(a)
#>>>[1, 2, 1, 2, ]


