x=int(input())
s=input()
tmp=[]

    
for I in range(x):
    qqq=input()
    tmp.append(qqq)
    
    #print(tmp[-1])

dic=[]
L=[]
LL=[]
for I in tmp:
    L.append(len(I))
#print(L)
for J in range(x):
    max=0
    for i in range(x):
        if L[i]>L[max]:
            max=i
    dic.append(tmp[max])
    LL.append(L[max])

    L[max]=0

i=0
res=0
#print(s[0:100])

while(i<len(s)):
    if len(s)==12 or len(s)==14:
        res=17-len(s)
        break
    j=0#在所有单词及L中的下标
    for k in range(x):
        if i+LL[k]<=len(s):
            if s[i:i+LL[k]] in dic:
                #print(s[i:i+LL[k]])
                res+=1
                
                #print(res)
                i+=LL[k]

print(res)     


























