n=int(input())
num=list(map(int,input().split()))
num.reverse()
out=[]
for i in num:
    if(i not in out):
        out.append(i)
out.reverse()
print(len(out))
for i in range(len(out)):
    if(i!=len(out)-1):
        print(out[i],end=" ")
    else:
        print(out[i])