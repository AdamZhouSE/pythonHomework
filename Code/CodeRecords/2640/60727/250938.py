S= input()
S=str(S)
T=input()
res="1"*500
l = len(S)
for i in range(0,l-len(T)):
    for j in range(i,l):
        count=0
        temp = S[int(i):int(j+1)]
        for m in T:
            if m in temp:
                count+=1
        if count==len(T) and j-i+1<len(res):
            res=S[i:j+1]

print(res)