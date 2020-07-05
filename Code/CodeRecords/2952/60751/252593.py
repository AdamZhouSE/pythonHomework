def sub(x,y,list):
    if int(x)>len(list) or int(y)>len(list):
        return 0
    str1=list[int(x)-1]
    str2=list[int(y)-1]
    if len(str1)>len(str2):
        return 0
    count=0
    for i in range(len(str2)-len(str1)+1):
        if str1==str2[i:i+len(str1)]:
            count=count+1
    return count
def _print(str):
    list=[]
    _str=""
    for i in str:
        if i=="P":
            list.append(_str)
        elif i=="B":
            _str=_str[0:-1]
        else:
            _str=_str+i
    return list
str=input()
num=input()
list=_print(str)
for i in range(int(num)):
    list2=input().split(" ")
    x=list2[0]
    y=list2[1]
    print(sub(x,y,list))