# import os
# import shutil
# import re
#
#
# path_img=r'E:\ikangDATA\CTData_v1.3\Annotations'
# file = open("../keras-yolo3-master/delwith/right.txt","r")
# lines = file.readlines()
# for line in lines:
#     line1=re.split("\n",line)[0]
#     print(line1)
import sys
# print(sys.version_info[0])

# def func(x):
#     return x*x;
#
# a= map(func,[1,2,3,4,5,6])
# print(type(a))

from functools import reduce
def func1(a,b):
    return a+b

a = reduce(func1,[i for i in range(0,101)])
print(a)

list1 = [1,3,4,66,5]
print(sorted(list1,key=abs,reverse=True))
print(list1)

print("test_here_is:",__file__,sys._getframe().f_lineno)


list2 = [3,4,5,6,7,8]
i1 =iter(list2)

print(i1.__next__(),i1.__next__())
print("test_here_is:",__file__,sys._getframe().f_lineno)

# list3 = [i for i in range(0,101)]
# l2 = iter(list3)
# while l2 is not None:
#     print(next(l2))
list3 = [i for i in range(0,101)]
list4 = (i for i in range(0,101))
list5 = (3,4,5,6,7)
print(type(list3))
print(type(list4))
print(type(list5))
print(next(list4),next(list4))
# print(next(list5),next(list5))
print("test_here_is:",__file__,sys._getframe().f_lineno)


def func2():
    for x in range(5, 10):
        yield x+4
        # print("x = %d"%x)

g = func2()
print(g.__next__())
print(next(g))
for dd in func2():
    print(dd)