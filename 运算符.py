"""
基本运算符
基本练习 ctrl+/ 单行注释快捷键
这是一个多行注释
"""
# 这是一个单行注释
a = 21
b = 10
c = 0
c = a + b
print ("line 1 -value of c is",c)
c = a - b
print ("line 2 -value of c is",c)
c = a * b
print ("line 3 -value of c is",c)
c = a / b
print ("line 4 -value of c is",c)
c = a % b
print ("line 5 -value of c is",c)
a = 2
b = 3
c = a ** b
print ("line 6 -value of c is",c)
a = 10
b = 5
c = a // b
print ("line 7 -value of c is",c)
# 比较运算符
a = 21
b = 10
c = 0

if a == b:
    print ("line 1 - a 等于 b")
else:
    print ("line 1 - a 不等于 b")

if a != b:
    print ("line 2 - a 不等于 b")
else:
    print ("line 2 - a 等于 b")
if a > b:
    print("line 4 - a 大于 b")
else:
    print("line 4 - a 小于 b")
if a < b:
    print("line 5 - a 小于 b")
else:
    print("line 5 - a 大于 b")
if a >= b:
    print("line 6 - a 大于等于 b")
else:
    print("line 6 - a 小于等于 b")
if a <= b:
    print("line 7 - a 小于等于 b")
else:
    print("line 7 - a 大于等于 b")
# 赋值运算符
a = 21
b = 10
c = 0
c = a + b
print("line 1 - c 的值为：",c)
c += a
print("line 2 - c 的值为：",c)
c -= a
print("line 3 - c 的值为:",c)
c *= a
print("line 4 - c 的值为:",c)
c /= a
print("line 6 - c 的值为:",c)
c %= a
print("line 7 - c 的值为：",c)
c **= a
print("line 8 - c 的值为:",c)
c //= a
print("line 9 - c 的值为:",c)
# 位运算符
a = 60   # 60 = 0011 1100
b = 13   # 13 = 0000 1101
c = 0
c = a & b ; # 12 = 0000 1100
print("line 1 - c 的值为:",c)
c = a | b;  # 61 = 0011 1101
print("line 2 - c 的值为:",c)
c = a ^ b; # 49 = 0011 0001
print("line 3 - c 的值为:",c)
c = ~a; # -61 = 1100 0011
print("line 3 - c 的值为:",c)
c = a << 2; # 240 = 1111 0000
print("line 5 - c 的值为:",c)
c = a >> 2; # 15 = 0000 1111
print("line 6 - c 的值为:",c)
# 逻辑运算符
a = 10
b = 20
if ( a and b):
    print("line 1 - 变量 a 和 b 都为 true")
else:
    print("line 1 - 变量 a 和 b 有一个不为 ture")
if ( a or b):
    print("line 2 - 变量 a 和 b 都为 true")
else:
    print("line 2 - a 和 b 都不为 true")
# 修改变量a的值
a = 0
if ( a and b):
    print("line 3 - 变量 a 和 b 都为 true")
else:
    print("line 3 - 变量 a 和 b 有一个不为 true")
if ( a or b):
    print("line 4 - 变量 a 和 b 都为 true , 或其中一个变量为 true")
else:
    print("line 4 - 变量 a 和 b 都不为 true")
if not( a and b):
    print("line 5 - 变量 a 和 b 都为 flase,或其中一个变量为 false")
else:
    print("line 5 - a 和 b 都为true")
# 成员运算符
a = 10
b = 20
list =[1,2,3,4,5]; 
if( a in list ):
    print("line 1 - 变量 a 在给定的列表中 list 中")
else:
    print("line 1 不在给定的列表中 list中")
if ( b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")
# 修改变量 a 的值
a = 2
if ( a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")


 
