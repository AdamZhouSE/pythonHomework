s = input()              #输入 得到str格式的数据
info = s.split('+')      #按照+号分割字符串，info是列表里面存放输入当中的数字
a = []  
for num in info:
    a.append(int(num))   #循环按照int格式保存下info中的数字，保存在a中 
a.sort()                 #排序
b = []
for aa in a:   
    b.append(str(aa))    #按照str格式保存下a中的数字
print('+'.join(b))     #用+号把b中的数字连接起来，返回的是一个str 