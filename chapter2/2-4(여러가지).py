#불 참,거짓
a = 1 == 1
print(type(a))
#>>><class 'bool'>   불 자료이다.

a = 1 == 1
print(a)
#>>>True     1은 1이니?? 답:True
a = 1 == 2
print(a)
#>>>False     2는 1이니?? 답:False

# "python"	참
# ""	    거짓
# [1, 2, 3]	참
# []	    거짓
# (1, 2, 3)	참
# ()	    거짓
# {'a': 1}	참
# {}	    거짓
# 1  	    참
# 0	        거짓
# None	    거짓

a, b = ('python', 'life')
print(a)
print(b)
#>>>python
#   life

a = b = 'python'
print(a)
print(b)
#>>> python
#    python

#값을 바꾸기
a = 3
b = 5
a,b = b,a
print(a)
print(b)
#>>>5
#   3
