def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

n=int(input())
ar=input()
ar=nums(ar)
answer=[0 for i in range(n)]
for i in range(n):
    m=ar.count(ar[i])
    if m>1:
        indicate=0
        for j in range(n):
            if ar[j]==ar[i]:
                indicate+=1
                if indicate==m:
                    answer[j]=ar[i]
                    break
    else:
        answer[i]=ar[i]
n=0
for v in answer:
    if v!=0:
        n=n+1
print(n)
string=''
for v in answer:
    if v!=0:
        string+=str(v)+' '
print(string.rstrip())