#1、func list()
print("======func list()")
print(list('Hello'))


#2、Modify list: Assign values to elements
print("\n======Assign values to elements")
lst = [1,3,5,7,9]
lst[1] = '2'
print(lst)


#3、del elements
print("\n======del elements")
lst_3 = [1,2,3,4,5,6,7,8,9]
del lst_3[4]    # Del the value 5(index 4)
print(lst_3)


#4、Assign values to slice
#   The length of list is changeable
print("\n======Assign values to slice")
lst_4 = list('perl')
lst_4[2:] = list('aj')
print(lst_4)
lst_4[:1] = list("asdfg")
print(lst_4)
lst_4[1:3] = list('a')
print(lst_4)


#5、func append():Add a obj(or element) to the end of list
print("\n======func append()")
lst_5 = [1,2,3,4,5,6,7,8,9]
lst_5.append('2')           # add a element
print(lst_5)
lst_5.append(list('asdg'))  # add a obj
print(lst_5)


#6、func clear():Clear the contents of list
print("\n======func clear()")
lst_6 = [123,415,152]
lst_6.clear()
print(lst_6)


#7、func copy():copy list
print("\n======func copy()")
a7 = [1,2,3,4,5,6]  
b7 = a7     # a7和b7指向同一个列表      
print(b7)   
c7 = a7.copy()  # c7和a7指向不同得列表，只是列表得内容相同
print(c7)
b7.clear()
print(b7)
print(a7)
print(c7)


#8、func extend():extend list
print("\n======func extend()")
a8 = [1,2,3]
b8 = [4,5,6]
a8.extend(b8)
print(a8)
print(b8)
# 拼接
a8 + b8
print(a8)
print(b8)
# 拼接实质
a8[len(a8):] = b8
print(a8)


#9、func count(): Count times of the specified element appears in the list
print("\n======func extend()")
li9 = [1,2,3,4,5,6,1,2,3,1,2,3,1,2,3]
num = li9.count(3)
print('3在列表中出现了', num , '次')


#10、func index(): Find the first index of the specified element appears in the list
print("\n======func index()")
letter = ['fir','sec','thi','fou','fiv','sec']
idx = letter.index('sec')
print(idx)


#11、func insert(): Insert a obj(or element) to the specified position of list
print("\n======func insert()")
lst_11 = [1,2,3,4,5,6]
lst_11.insert(3, 'four')
print(lst_11)


#12、func pop(): Del the last element of list, and return the last element. 
print("\n======func pop()")
lst_12 = ['1',2,26,258]
ret_12 = lst_12.pop()
print(ret_12)


#13、func remove(): Del the first specified element of list, return none
print("\n======func remove()")
lst_13 = [1,2,3,4,5,1,2,3,4,5]
lst_13.remove(3)
print(lst_13)


#14、func reverse(): reverse all elements
print("\n======func reverse()")
lst_14 = [1,2,3]
lst_14.reverse()
print(lst_14)


#15、func sort():Sort all elements, return none
print("\n======func sort()")
lst_15 = [1,5,2,6,3,4]
lst_15.sort()
print(lst_15)
# sort by the element length
len_lst = ['s','dfdf','fv','fgh','d','gb','wewds']
len_lst.sort(key = len)
print(len_lst)
# reverse sort
lst_15.sort(reverse = True)
print(lst_15)


# tuple
print("\nTuple:=======")
tpl = (42,32)
print(tpl)
print(tpl*6)
# convert list to tuple
print(tuple([1,2,3]))