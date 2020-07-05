def findMax(list):
    max=0
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
    return max

def isNotEqual(list):
    for i in range(len(list)-1):
        if list[i]!=list[i+1]:
            return True
    return False

list=list(map(int,input().split(',')))
max=findMax(list)
result=0
while isNotEqual(list):
    result+=1
    for i in range(len(list)):
        if list[i]==max:
            max+=1
        else:
            list[i]+=1
    max=findMax(list)
print(result)