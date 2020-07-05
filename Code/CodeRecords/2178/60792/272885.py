def count(list1,k):
    list2=[]
    for i in range(0,k+1):
        for j in range(i+1,k+2):
            if list1[i:j] not in list2:
                list2.append(list1[i:j])
    return len(list2)   

n=int(input())
list1=list(map(int,input().split(" ")))
for i in range(0,len(list1)):
    print(count(list1,i))