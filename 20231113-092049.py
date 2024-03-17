#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
# format type data
nmb1 = 301
nmb2 = 3822
print(f"This is my number {nmb1+nmb2}")
x = 202
y = 3123
print(x>y)

#string type deta
print("kawsar")
name = 'Gamer'
print(name)
print(type(name))


#list type deta
li = ['kawsar','ami','tumi','who']
print(li)
print(type(li))

#tuple type deta
tup = (10,73,28,22,22)
print(tup)
print(type(tup))

#range type data
ran = range(6)
for i in ran:
    print(i)
print(type(ran))

#