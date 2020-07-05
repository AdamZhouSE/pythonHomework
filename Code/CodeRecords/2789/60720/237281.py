time=int(input())
for i in range(time):
    size=int(input())
    list=input().split()
    for j in range(size):
        list[j]=int(list[j])
    list.sort(reverse=True)
    isE=False
    for j in range(size-1):
        if list[j]>=j+1 and list[j+1]<j+2:
            print(j+1)
            isE=True
            break
    if(isE==False):
        print(size)
    isE=False