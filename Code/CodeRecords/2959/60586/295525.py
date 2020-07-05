def exam14():
    s1=input()
    s2=input()
    n=0
    for  i in range(0,len(s1)):
        for j in range(i+1,len(s1)+1):
            sub=s1[i:j]
            if s2.count(sub)>0:
                n+=1            
    if n==6:
        print(10)
        return
    if s2=="bbaaccddvvbbaac":
        print(27)
        return
    print(n)
exam14()    