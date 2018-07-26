#coding: utf-8
#能输出完整的字典格式
dict={
    '姓名':'大哥大',
    '年龄':20,
    '学号':'1627405110'
}
line = None
for key in dict:
    if line != None:
        line += ','
    else:
        line = '{'
    line += "'" + key +"':" + str(dict[key])
line += '}'
print line              #字典中是无序的


'''
#确保字典中中文的输出
#coding: utf-8
dict={
    '姓名':'大哥大',
    '年龄':20,
    '学号':'1627405110'
}
for key in dict:
    print key+':'+dict[key]
'''
