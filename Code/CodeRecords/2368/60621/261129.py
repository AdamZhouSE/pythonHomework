a=eval(input())
for i in range(a):
    num = eval(input())
    temp = [int(x) for x in input().split()]
    store=0
    j=0
    for k in range(num//2):
        temp.insert(j,temp[len(temp)-1])
        temp.pop()
        j+=2
    for j in temp:
        print(j,end=" ")
    print("",end="\n")