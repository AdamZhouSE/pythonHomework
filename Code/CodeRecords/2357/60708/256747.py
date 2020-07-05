def check(a,b,X):
    if int(a)+int(b)==X:
        return True
    else:
        return False
N=int(input())
for n in range(0,N):
    temp=input().split(" ")
    l1=int(temp[0])
    l2=int(temp[1])
    X=int(temp[2])
    list1=input().split(" ")
    list2=input().split(" ")
    result=[]
    for a in range(0,l1):
        for b in range(0,l2):
            if(check(list1[a],list2[b],X)):
                temp=[]
                temp.append(list1[a])
                temp.append(list2[b])
                result.append(temp)
    for item in result:
        print(item[0],item[1])
