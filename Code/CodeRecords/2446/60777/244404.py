n=int(input())
str=[]

for i in range(n):
    str.append(input().split())
    
l=int(input())

for i in range(l):
    find=False
    temp=input()
    for j in range(n):
        if(temp in str[j]):
            print(j+1,end=" ")
            find=True
    if(find==False):
        print(" ",end='')
    print()