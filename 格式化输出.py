#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/20 9:00
# @Author  : zhengjunhui
# @Email    : zhengoba@foxmail.com
name = raw_input('name:')
age = raw_input('age:')
job = raw_input('job:')
#第一种，字符串拼接 利用%进行定义替换
print "开始执行第一种"
suminfo = '''
======================print message=====================
         name :%s
         age :%s
         job :%s
======================print end==========================
'''
print suminfo %(str(name),int(age),str(job))

#第二种 format函数 通过关键字参数 格式化输出
print "开始执行第二种"
suminfo2 = '''
======================print message=====================
         name :{name}
         age :{age}
         job :{job}
======================print end==========================

'''.format(name=str(name),age=int(age),job=str(job))           #利用这种=号赋值的方式位置可以不按顺序
                                                #利用{}号来代替字符串或其他数据类型，用 .format函数定义或者引用变量值作为参数复值到{}中的值
                                                # .formact函数不限参数个数
print suminfo2

#第三种 format函数 通过位置 格式化输出
#listP = ('name','age','job')
suminfo3 = '''
======================print message=====================
         name :{0}               #这里的数字代表要获取format里参数的索引值 0就是索引为0位置的参数，也就是参数name的值。
         age :{1}
         job :{2}
======================print end==========================

'''.format(str(name),int(age),str(job))

print suminfo3
#第四种 format函数 通过下标位置 格式化输出

listP = [name,age,job]
suminfo4 = '''
======================print message=====================
         name :{0[0]}               #这里的第一个数字0代表要获取format里参数的索引值 也就是listP的值 所以只能写成0 如果写成其他值 会报下标越界。
         age :{0[1]}                #第二个位置的数字代表要取的listP列表的下标位置
         job :{0[2]}
======================print end==========================
#通过这种方式可以轻松的传递list/tuple/dict给format函数
'''.format(listP)
print suminfo4

