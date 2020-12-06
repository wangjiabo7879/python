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


# 格式填充：零、加号、减号或者空格
print("{:010.3f}".format(3.141592657))
print("{:->10.2f}".format(3.141592657))
print("{:+>10.2f}".format(3.141592657))
print("{:$^10.2f}".format(3.141592657))
# "=": 将填充字符放在符号与数字之间
print("{:$=10.2f}".format(-3.141592657))

# 对齐形式：左对齐(<)、右对齐(>)、居中(^)
print("左对齐{:<10.2f}".format(3.141592657))
print("右对齐{:>10.2f}".format(3.141592657))
print("居中  {:^10.2f}".format(3.141592657))









