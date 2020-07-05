a=int(input().strip())
for i in range(a):    
    s=input()
    t=input()
    se=set(list(t))
    li=list(se)
    standard1=[]
    standard2=[]
    for i in li:
        standard1.append(t.count(i))
        standard2.append(s.count(i))
    com=[int(standard2[i]/standard1[i]) for i in range(len(standard1))]
    print(min(com))
    
    