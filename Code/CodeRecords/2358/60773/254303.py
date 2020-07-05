num=int(input())
for k in range(num):
    s1=input()
    l1=s1.split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    s2=input()
    l2=s2.split(" ")
    for i in range(len(l2)):
        l2[i]=int(l2[i])
        
    l2.sort()
    for i in range(n2):
        print(l2[len(l2)-1-i],end=" ")
    print("")