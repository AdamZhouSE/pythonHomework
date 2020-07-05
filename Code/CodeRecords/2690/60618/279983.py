t=int(input())
for i in range(0,t):
    n,m=map(int,input().split())
    s,s2=map(str,input().split())

    s1=list(s)
    for j in range(0,len(s1)):
        if s1[j] not in s2:
            s1[j]='0'
    re=''.join(s1)
    result = re.split('0')
    sum=''.join(result)
    
    #result=[x.strip() for x in result if x.strip()!='']
    print(len(sum)//len(s2))