# ***字符串练习***
var1 = "study"
var2 = "hello word"
print(var1[1],var2[-1])
print(var1[1:4],var2[4::2])
print(var2[4::-2])
print(var1+"hehe")
print(var2[3:]+"fff")
print(var1+var2)
print(var1*2)
print("e" in var2)
print("u" not in var1)
if("t" in var1):
    print("t 在变量var1中")
else:
    print("t 不在变量var1中")
print(r"\n")
print("******************************")
print(var1.capitalize()) #将字符串的首字母转化为大写
print(var1.center(25,))  
print(len(var1))   # 展示字符串的长度
var3 = "HeLLO Word"
# 将字符串中的所有大写转化为小写
print(var3.lower())
print("\n")
# ***列表练习***
list1 = ["hehe","haha",2017,2018]
list2 = [1,2,3,4,5,6]
print(list1[1],list1[-1])
print(list1+list2)
print(list2[2:4])
# 删除列表中的指定元素
del list2[2]
print("删除列表中第三个元素",list2)
print(list1[1])
# 列表元素替换
list1[2]="MMM"
print(list1)
# 嵌套列表
n =[list1,list2]
print("列表n为：",n)
print(n[0])
print(n[0][1])
# 列表函数
print("列表长度",len(list2))
print("列表最大值：",max(list2))
print("列表最小值：",min(list2))
# 列表方法
print("添加新对象：",list2.append("oo")) # 直接把方法打印是错误的
print("\n")
list =["rubi","MMM","yili",5,6]
print("列表长度:",len(list)) # 列表函数
list.append("坏蛋")
print("添加新对象：",list)  # 列表方法
list.count(5)
print("次数：",list.count(5))
list.index("坏蛋")
print("坏蛋的索引为：",list.index("坏蛋"))
list.insert(4,"ok")
# print("插入数据：",list.insert(4,"ok"))  错误的写法
print("插入值：",list)
list.pop()
print(list)
list.pop(1)
print(list)
list.remove(5)
print("现在的列表为：",list)
list.reverse()
print("反转后的列表",list)
# list.sort()
# print("排序：",list)  不支持列表在字符串和整数同时存在时进行排序
u =list.copy()
print("复制列表u：",u)
list.clear()
print("清空列表",list)



