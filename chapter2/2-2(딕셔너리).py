#딕셔너리
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)
#>>>{'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {1: 'a'}
a[2] = 'b'
print(a)
#>>>{1: 'a', 2: 'b'}

#딕셔너리 안의 값을 없앨때
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
del a['name']
print(a)
#>>>{'phone': '010-9999-1234', 'birth': '1118'}

#Key의 값을 가져오고 싶을때
a = {1:'c', 2:'b'}
print(a[1])
#>>>c

#예시
seongju = {'name':'성주', 'phone':'010-1111-2222', 'birth':'123'}
print(seongju)
#>>>{'name': '성주', 'phone': '010-1111-2222', 'birth': '123'}
seongju = {'name':'성주', 'phone':'010-1111-2222', 'birth':'123'}
print(seongju['name'])
#>>>성주

#get을 이용해 값 가져오기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('phone'))
#>>>010-9999-1234
#다른 이용방법
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('이름',"값이 없습니다."))
#>>>값이 없습니다.
#이름이라는 key가 없기 때문에 값이 없습니다가 나온다.

#key가 같을때는 뒤에값이 앞에값을 덮어버린다.
a = {1:'a', 1:'b'}
print(a)
#>>>{1: 'b'}

#key의 내용을 가져오고 싶을때
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
#>>>dict_keys(['name', 'phone', 'birth'])

#key를 리스트로 뽑고싶을때
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(list(a.keys()))
#>>>['name', 'phone', 'birth']

#밸류만 가져오고 싶을때
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.values())
#>>>dict_values(['pey', '010-9999-1234', '1118'])

#key와 밸류를 합쳐서 가져오고 싶을때
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.items())
# >>>dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth','1118')])

