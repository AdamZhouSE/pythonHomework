
l=list(input())
k=int(input())
index=0
Max=width=k+1
while True:
    if index+width>len(l):
        break
    tmp=l[index:index+width]
    tmp=sorted(tmp,key=lambda x:tmp.count(x))
    if tmp.count(tmp[-1])+k>width:
        width+=1
        Max=width
    else:
        index+=1
        width+=1
print(Max)