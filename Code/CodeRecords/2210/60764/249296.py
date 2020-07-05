T=int(input())
for t in range(T):
    str1=input()
    str2=input()
    start,end=0,1
    res=""
    while True:
        check=True
        for i in range(len(str2)):
            if str2[i] not in str1[start:end]:
                check=False
                break
        if check==False:
            if end==len(str1):
                break
            end+=1
        else:
            if res=="" or len(res)>len(str1[start:end]):
                res=str1[start:end]
            start+=1
    if res=="":
        print(-1)
        print()
    else:
        print(res)
