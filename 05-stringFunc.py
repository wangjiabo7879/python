# -*- coding: utf-8 -*-
"""
    String functions
"""

'''
    1、center(): 在两边添加填充字符(默认为空白)让字符居中
       ljust(): 字符向左靠齐，向右填充字符
       rjust(): 字符向右靠齐，向左填充字符
       zfill(width)：在字符串左边填充0(但将原来打头的+或-移到开头)
'''
string_center = 'hello world!'
print(string_center.center(30))
print(string_center.center(30,"*"))
print(string_center.ljust(30))
print(string_center.ljust(30,"*"))
print(string_center.rjust(30))
print(string_center.rjust(30,"*"))
print(string_center.zfill(30))


'''
    2、(1)find(substr[,start[,end]])：在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
         @substr: 要搜索的子串。
         @start:  搜索起点
         @end:    搜索终点
       (2)rfind(substr[,start[,end]]): 返回最后一个子串的索引，如果没有就返回-1
'''
string_find = 'Hello, world! I am a programmer！'
print(string_find.find('a'))
print(string_find.find('x'))
print(string_find.find('a', 17))
print(string_find.rfind('a'))


'''
    3、(1)index(substr[,start[,end]]): 返回第一个sub的索引，如果没有就引发ValueError异常
       (2)rindex(substr[,start[,end]]): 返回最后一个sub的索引，如果没有就引发ValueError异常 
'''
string_index = 'asdfasdfasdf'
print(string_index.index('a'))
print(string_index.rindex('a'))


'''
    4、count(substr[,start[,end])：计算子串出现的次数
'''
str_cnt = 'aabbaasdbdnaabhnaabbkoljdnjcbbhheud'
print(str_cnt.count('bb'))


'''
    5、(1)startswith(prefix[,start[,end]): 检查字符串是否以prefix打头；还可将匹配范围限制在索引start和end之间
       (2)endswith(suffix[,start[,end])：检查字符串是否以suffix结尾；还可将匹配范围限制在索引start和end之间
'''
str_with = 'with width wide teth'
print(str_with.startswith('wi'))
print(str_with.endswith('wi'))
print(str_with.endswith('th'))


'''
    6、join(sequence): 用于合并序列的元素
       split(sequence): 用于分割字符串 --return list
'''
seq1 = '+'
seq2 = 'ghjk'
seq3 = seq1.join(seq2)
print(seq3) 
print(seq1)
print(seq2)
seq4 = seq3.split(seq1)
print(seq4) 


'''
    7、 lower(): 将字符串全部变为小写
        islower(): 检查字符串中的字母是否都是小写
        istitle(): 检查字符串位于非字母后面的字母都是大写的，且其他所有字母都是小写
        isupper(): 检查字符串中的字母是否都是大写的
'''
print('HYUJjidj'.lower())
print('sdsD'.islower())
print('搭建WJDcdjns降低'.title())
print('搭建WJDcdjns降低'.istitle())     # return False
print('搭建Wcdjns降低'.istitle())       # return True
print('jdA'.upper())
print('jdA'.isupper())


'''
    8、replace(old,new[,max]): 替换字符串中的子串
        @old: 要替换的子串
        @new：要替换的内容
        @max: 最大替换次数
'''
print('hello,world'.replace('lo','kx'))


'''
    9、strip([chars]): 将字符串开头和结尾的所有chars字符[默认为所有空白字符]都删除，并返回结果
'''
print('    chbs   '.strip())
print('    chbs   '.lstrip())
print('    chbs   '.rstrip())
print('ifs sdchbs  a'.strip('if'))

