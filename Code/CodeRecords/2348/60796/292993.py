def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j][0]>ls[j+1][0] or(ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j]=ls[i][j]+1
    return ls

def canmove(ls):
    n=ls[0]
    m=ls[1]
    canleft=True
    canright=True
    canup=True
    candown=True
    if m==0:
        canleft=False
    if canleft and not barrier.__contains__([n,m-1]):
        return True
    if m==M-1:
        canright=False
    if canright and not barrier.__contains__([n,m+1]):
        return True
    if n==0:
        canup=False
    if canup and not barrier.__contains__([n-1,m]):
        return True
    if n==N-1:
        candown=False
    if candown and not barrier.__contains__([n+1,m]):
        return True
    return False


nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
barrier=[]
for i in range(N):
    s=input()
    for j in range(M):
        if s[j]=='#':
            barrier.append([i,j])
#i+j偶数为黑点，奇数为白点
even=[]
odd=[]
cant=[]#不能走的点
print(barrier)
for i in range(N):
    for j in range(M):
        if not barrier.__contains__([i,j]):
            if not canmove([i,j]):
                cant.append([i,j])
            else:
                if (i+j)%2==0:
                    even.append([i,j])
                else:
                    odd.append([i,j])
result=[]+cant
if len(even)>len(odd):
    result=result+even
elif len(odd)>len(even):
    result=result+odd
print(result)
if len(result)==0:
    print(0)
else:
    result=bubble(result)
    print(len(result))
    for i in range(len(result)):
        s=str(result[i][0])
        for j in range(1,len(result[i])):
            s=s+" "+str(result[i][j])
        print(s)
















