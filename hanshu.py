# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs(28))


# def hello(name):
#     return 'hello,' + name + '!'
#
# print(hello("Winny"))

# def nop():
#     pass


# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs(1,2))


# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs('A'))







# import math
# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
#
# nx,ny=move(100,100,60,math.pi/6)
# print(nx,ny)
#
# n=move(100,100,60,math.pi/6)
# print(n)





#x=(-b+math.sqrt(d))/2a    d=b*b-4ac

# import math
# def quadratic(a,b,c):
#     if not isinstance(a,(int,float)):
#         raise TypeError('a ia not a number')
#     if not isinstance(b,(int,float)):
#         raise TypeError('b is not a number')
#     if not isinstance(c,(int,float)):
#         raise TypeError('c is not a number')
#     d=b*b-4*a*c
#     if a==0:
#         if b==0:
#             if c==0:
#                 return '方程的根为全体实数'
#             else:
#                 return '方程无根'
#         else:
#             x1=-c/b
#             x2=x1
#             return x1,x2
#     else:
#         if d<0:
#             return '方程无根'
#         else:
#             x1=(-b+math.sqrt(d))/(2*a)
#             x2=(-b-math.sqrt(d))/(2*a)
#             return x1,x2
# print(quadratic(2,3,1))




# def power(x):
#     return x*x
# print(power(2))


# def power(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print(power(5))


# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L
# # print(add_end([1,2,3]))
# print(add_end())
# print(add_end())
# print(add_end())


#a*a+b*b+c*c+......
# def cals(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# print(cals(1,2,3,4))

# nums=[1,2,3]
# def cals(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# print(cals(nums[0],nums[1],nums[2]))
# print(cals(*nums))


# extra={'city':'Beijing','job':'Engineer'}
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# person('Winny',24,**extra)


# def person(name,age,**kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:',name,'age:',age,'other:',kw)
# person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)


# def person(name,age,*,city,job):
#     print(name,age,city,job)
# person('Jack',24,city='Beijing',job='Engineer')


# def person(name,age,*,city='Beijing',job):
#     print(name,age,city,job)
# person('Jack',24,job='Engineer')



# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# f1(1,2,3,'a','b',x=99)

# def f2(a,b,c=0,*,d,**kw):
#     print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
# f2(1,2,d=99,ext=None)



# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# args=(1,2,3)
# kw={'d':99,'x':'#'}
# f1(*args,**kw)




# def f2(a,b,c=0,*,d,**kw):
#     print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
# args=( 1,2,3)
# kw={'d':88,'x':'#'}
# f2(*args,**kw)



















































































