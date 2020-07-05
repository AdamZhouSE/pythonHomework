n=int(input())
fn=input().split(" ")
fn=list(int(a) for a in fn)
res="NO"
for i in range(0,n):
    if(fn[fn[fn[i]-1]-1]==i+1):
        res="YES"
        break
print(res)