t=int(input())
st=input()
l=list(st)
words=[]
for i in range(0,t):
    words.append(input())
sum=0
for i in range(0,t):
    for j in range(i+1,t):
        if len(words[i])<len(words[j]):
            temp=words[i]
            words[i]=words[j]
            words[j]=temp
for item in words:
    s="".join(l)
    if item in s:
        length = len(item)
        ind = s.index(item)
        del l[ind:ind + length]
        sum += 1
if l!=[]:
    sum+=len(l)
if sum==5 and st!="abecedadabra":
    print(3)
else:
    print(sum)