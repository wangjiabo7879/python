'''
    dict(): 从其他映射或键值对序列创建字典
'''
item_1 = [('name','jobw'),('age','23')]
print('dict1=',dict(item_1))
print('dict20',dict(name='jobw',age=23))

# 成员资格访问符号：查找的是键不是值
print('name' in dict(item_1))   # Return Ture
print('jobw' in dict(item_1))   # Return False



'''
    clear(): 删除所有的字典项
'''
dic_2 = {'name':'jobw','age':'23'}
dic_2.clear()
print(dic_2)



'''
    copy(): 浅拷贝，返回一个字典。替换副本中的值不影响原件，增删副本中的值影响原件。
    deepcopy(): 深拷贝,同时复制值及其包含的所有值。在copy模块中
'''
copy_self = {'name':'jobw',
             'age':['12','23','34']}
copy_other = copy_self.copy()
print(copy_other)
copy_other['name'] = 'jobz'
print(copy_other)
copy_other['age'].remove('23')
print(copy_other)
print(copy_self)

from copy import deepcopy
copy_self = {'name':'jobw',
             'age':['12','23','34']}
copy_other = deepcopy(copy_self)
print(copy_other)
copy_other['age'].remove('23')
print(copy_other)
print(copy_self)



'''
    fromkeys(): 创建一个新字典，其中包含指定的键，且每个键对应的值都是None
'''
item_list = ['name','sex','age','score']
dic_none = {}
print(dic_none.fromkeys(item_list))
# 改变默认值
item_list = ['name','sex','age','score']
dic_none = {}
print(dic_none.fromkeys(item_list,'改变默认值'))



'''
    get(key): 获取字典中键的值，如果键不存在，则返回none
'''
dic_none = {'name': '改变默认值', 'sex': '改变默认值', 'age': '改变默认值', 'score': '改变默认值'}
print(dic_none.get('sex'))
print(dic_none.get('nji'))



'''
    items(): 返回一个包含所有字典项的列表，其中每个元素都为（key,value）形式
    keys(): 返回一个字典视图，其中包含指定字典中的键
    values(): 返回一个字典视图，其中包含指定字典中的值
    pop(key): 获取与指定键相关联的值，并将该键值对从字典中删除
'''
it = {'name': 1, 'sex': 2, 'age': 3, 'score': 4}
print(it.items())   # 返回字典视图
print(('score', 4) in it.items())
print(it.keys())
print(it.values())
print(it.pop('sex'))
print(it)



'''
    popitem(): 随机弹出一个字典项，并删除
'''
dicpop = {'qwe':12,'23':'age'}
print(dicpop.popitem())
print(dicpop)



'''
    setdefault(): 获取与指定键相关联的值，
                若存在，则返回指定的值
                若不存在，则在字典中添加指定的键值对
'''
ds = {}
ds.setdefault('name', 'job')
print(ds)
print(ds.setdefault('name', 'job'))


'''
    update(dict): 使用一个字典中的项来更新另一个字典,如果存在相同的键则修改
'''
dic1 = {'name':'jobw','age':23}
dic2 = {'sex':'f','age':25}
dic1.update(dic2)
print(dic1)
print(dic2)


