def sort(List):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
    return List


T=int(input())
for i in range(T):
    mnk=list(map(int,input().split(' ')))
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    c=a+b
    c=sort(c)
    print(c[mnk[2]-1])