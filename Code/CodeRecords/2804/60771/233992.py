#1
str = input()
if(len(str)>=1):
    str = str.replace('+','')
    #没有对字符串直接排序的方法，要转化成list才可以
    l = list(str)
    l.sort()
    str = "+".join(l)
    "+".join(str)
    print(str)
else:
    print(str)