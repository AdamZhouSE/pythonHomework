from sys import stdin 

def operate(list,p):
    if list[p+1]!=0 and list[p+1]==list[p] :
        list[p]*=2
        list[p+1]=0
    return resort(list)
        
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
    length=int(stdin.readline())
    list=[int(x) for x in stdin.readline().split()]
    list=resort(list)
    for j in range(0,length-1):
        list=operate(list,j)
    temp=iter(list)
    print(next(temp),end='')
    while True:
        c=next(temp,'p')
        if c!='p':
            print(" ",end='')
            print(c,end='')
        else:
            break
    print("")