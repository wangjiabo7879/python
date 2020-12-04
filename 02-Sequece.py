#1、序列的索引
print("=====序列的索引=====")
greeting = 'Hello'
print(greeting[0])      # 正数索引
print(greeting[-1])     # 负数索引
print('hello'[1])       # 不带变量索引


#2、序列的切片
#    (1) 第一个索引指定的元素包含在切片内，第二个索引指定的元素不包含在切片内
print("=====序列的切片=====")
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])        # http://www.python.org
print(tag[32:-4])       # Python web site
#    (2)省略第一个索引：即从序列的第一个元素开始
print(tag[:3])
#    (3)省略第二个索引序列：即取到序列的最后一个元素
print(tag[32:])
#    (4)两个索引都不写：即取得序列全部
print(tag[:])
#   (5)规定步长(默认情况下步长为1):第三个索引(可正可负)
print(tag[::5])     # 步长为5
print(tag[::-5])    # 反向取


#3、序列得乘法=copy
print("=====序列的切片=====")
print("Hello"*5)
print([1,2,3]*5)


#4、成员资格：检查特定得值是否包含在序列中，使用运算符in
#       - 满足返回True
#       - 不满足返回False
print("=====成员资格=====")
print('e' in 'Hello')
print('a' in 'Hello')
lst_4 = [['hoo','qwe'],['aoo','asd'],['zxc','dfg']]
print(['hoo','qwe'] in lst_4)


#5、内置函数：len(),min(),max()
print("=====内置函数=====")
numbers = [123,456,789]
print(len(numbers))
print(min(numbers))
print(max(numbers))















