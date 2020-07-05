g=int(input())
for k in range(0,g):
    string=input()
    SET=set(string)
    ans=0
    for i in range(len(SET),len(string)+1):
        for j in range(0,len(string)-i+1):
            s=set(string[j:j+i])
            if s==SET:
                ans=i
                break
        if ans!=0:
            break
    print(ans)


