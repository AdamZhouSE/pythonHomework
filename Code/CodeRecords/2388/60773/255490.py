num=int(input())
for k in range(num):
    n=int(input())
    s1=input()
    s2=input()
    l1=s1.split(" ")
    l2=s2.split(" ")
    l1.sort()
    l2.sort()
    if l1==l2:
        print(1)
    else:
        print(0)
