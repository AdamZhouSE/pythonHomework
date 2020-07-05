def check(List):
    for i in range(0,len(List)-1):
        if List[i]==List[i+1]and List[i]!=0:
            return True
    return False

Neq=int(input())
for i in range(0,Neq):
    l=int(input())
    temp=input().split(" ")
    List=[]
    for item in temp:
        List.append(int(item))
    x=0
    Zero=0
    while(check(List)):
        while (x < len(List) - 1):
            if List[x] == List[x + 1] and List[x] != 0:
                List[x] = List[x] + List[x + 1]
                List[x+1]=0
            x = x + 1
        x = 0
    Zero=0

    for item in List:
        if item!=0:
            print(item,end=" ")
        else:
            Zero=Zero+1
    for x in range(0,Zero-1):
        print(0,end=" ")
    print(0)