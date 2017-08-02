#!/user/bin/env python3
# -*- coding: utf-8 -*-

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%',只保留小数点后1位

#s1 = 72
#s2 = 85
#r = (s2-s1)/s1
#print('%.1f' % r)



#条件判断
#age=3
#if age>=18:
    #print('your age is',age)
    #print('adult')
#else:
   #print('your age is',age)
   #print('teenager')




# elif
# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')



#input()
# birth=input('Birth:')
# birth1=int(birth)
# if birth1<2000:
#     print('00前')
# else:
#     print('00后')



#练习
height=1.75
weight=80.5
#bmi=weight/height/height
bmi=weight/pow(height,2)
if bmi<18.5:
    print('过轻')
elif bmi>=18.5 and bmi<=25:
    print('正常')
elif bmi>25 and bmi<=28:
    print('过重')
elif bmi>28 and bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')





























