n1=int(input())
for i in range(n1):
    s=input().split(" ")
    n2=int(s[2])
    #print(n2)
    s1=input()
    s2=input()
    str=s1+" "+s2
    l=str.split(" ")
    result=[]
    for i in l:
        result.append(int(i))
    result.sort()
    #print(l)
    print(int(result[n2-1]))
    
    
