# def a(x):
#     def b():
#         return x+x
#     return b
#
# x= a('x')
# y=a('')
# print(x()+y())

# from datetime import timedelta
# delta=timedelta(weeks=1,days=7,hours=11)
# print(delta)
# d={}
# d['2']=[1,2]
# d['1']=[3,4]
#
# for x in d.keys():
#     print(d[x][1], end="")

# list=[1,2,3,4]
# list=list(map(lambda x:2*x,list))
# print(list)

# z=2
# y=1
# x=y<z or z>y and y>z or z<y
# print(x)

# x,y,z=3,2,1
# z,y,x=x,y,z
# print(x,y,z)

# def fun(n):
#     s=''
#     for i in range(n):
#         s+='*'
#         yield s
#
# for x in fun(3):
#     print(x, end='')

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
#
# print(issubclass(C,A) and issubclass(C,B))

# class X:
#     pass
# class Y(X):
#     pass
# class Z(Y):
#     pass
# x=X()
# z=Z()
#
# print(isinstance(x,Z) and isinstance(z,X))

# x=16
# while x>0:
#     print('*', end='')
#     x //= 2

# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")

# i=4
# while i>0:
#     i-=2
#     print("*")
#     if i==2:
#         break
#     else:
#         print("*")

a = True
b=False
a=a or b
b=a and b
a=a or b
print(a, b)
