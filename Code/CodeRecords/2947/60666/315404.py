n=int(input())
strin=input()
for i in range(n):
    lst=input().split()
    if int(lst[0])==1:
        strin+=lst[1]
        print(strin)
    elif int(lst[0])==2:
        strin=strin[int(lst[1]):int(lst[1])+int(lst[2])]
        print(strin)
    elif int(lst[0])==3:
        strin=strin[0:int(lst[1])]+lst[2]+strin[int(lst[1]):-1]
        print(strin)
    else:
        print(strin.find(lst[1]))