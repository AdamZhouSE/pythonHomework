li=list(eval(input()))
k=int(input())
l=[]
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        l.append((li[i],li[j],li[i]/li[j]))
l=sorted(l,key=lambda x:x[2])
print('['+str(l[k-1][0])+', '+str(l[k-1][1])+']')