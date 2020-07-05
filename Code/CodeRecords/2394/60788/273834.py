from sys import stdin
def resort(list):
    length=len(list)
    zero=list.count(0)
    new_list=[]
    for ele in list:
        if ele!=0:
            new_list.append(ele)
    for  i in range(0,zero):
        new_list.append(0)
    return new_list

num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    list=[int(x) for x in stdin.readline().split()]
    list=resort(list)
    temp=iter(list)
    print(next(temp),end='')
    while True:
        c=next(temp,'p')
        if c!='p':
            print(" ",end='')
            print(c,end='')
        else:
            break
    print(" ")
