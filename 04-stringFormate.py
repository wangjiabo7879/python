from math import e

# %s:转换说明符

fo = "Hello,%s,what do you %s?"
values = ('bob','like')
print(fo%values)


# 字符串format方法替换字段
print("{},{} and {}".format("first","second","third")) 
# 带索引
print("{2},{1} and {0}".format("first","second","third"))


# 变量与字段同名：直接在字符串前面加f
print(f"Euler's constant is roughly {e}")
# 上述语句等效于
print("Euler's constant is roughly {e}".format(e=e))


# 替换字段
print("{four},{sec},{},{}".format(1,2,sec=3,four=4))
print("{four},{1},{0},{sec}".format(1,2,sec=3,four=4))


#宽度设置:数字默认向左对齐，字符串默认向右对齐
print("{num:10}".format(num=9))
print("{num:10}".format(num='9'))

#精度设置
print("{num:8.3f}".format(num=3.141592657))
print("{num:8.3}".format(num='3.141592657'))

# 千位分隔符
print("One googol is {:,}".format(10**100))







