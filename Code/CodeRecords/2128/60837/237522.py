def circle(list):
    ex=list[len(list)-1]
    for i in range(len(list)-1):        
        list[len(list)-i-1]=list[len(list)-i-2]
    list[0]=ex
    
def Func(list):
    num=0
    for i in range(len(list)):
        num+=list[i]*i
    return num
    
list=list(map(int,input().split(',')))
max=0
for i in range(len(list)):
    if Func(list)>max:
        max=Func(list)
    circle(list)
print(max)