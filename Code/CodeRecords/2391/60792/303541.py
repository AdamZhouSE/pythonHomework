n=int(input())
list1=[]
for i in range(0,n):
    list1.append(input())
m=int(input())
list2=[]
for i in range(0,m):
    s=input()
    if s in list1:
        if s not in list2:
            print("OK")
            list2.append(s)
        else:
            print("REPEAT")
    else:
        print("WRONG")