t=int(input())
for i in range(t):
    s1,s2=input().split()
    num=0
    for j in range(len(s1)):
        for k in range(len(s2)):
            if(s1[j]==s2[k]):
                num+=1
    print(len(s1)+len(s2)-num)