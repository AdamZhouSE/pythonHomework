
def smallestlength(list1,list2):
    dict={}
    for j in range(len(list1)):
        if list1[j] not in dict:
            dict[list1[j]]=1
    for k in range(len(list2)):
        if list2[k] not in dict:
            dict[list2[k]]=1        
    return len(dict)    
    




T=int(input())
for i in range(T):
    str11,str22=input().split(' ')
    list1=list(str11)
    list2=list(str22)
    print(smallestlength(list1,list2))