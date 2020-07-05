n,p=map(int,input().split())
s=input().split(" ")
table=[True for i in range(0,p)]    #True表示空
for i in range(0,n):
    num=(ord(s[i][len(s[i])-3])-65)*(32**2)+(ord(s[i][len(s[i])-2])-65)*32+ord(s[i][len(s[i])-1])-65
    idx=num%p
    count=1
    time=0
    while not table[idx]:
        if time%2==0:
            idx+=count**2
        else:
            idx-=2*count**2
            if idx<0:
                idx=p-idx
            count+=1
        time+=1
    print(str(idx)+" ",end="")