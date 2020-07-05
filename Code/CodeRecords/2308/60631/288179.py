s=input().split(' ')
n=int(s[0])
root=int(s[1])
data=[]
for i in range(100):
    data.append(-1)
data[1]=root
for i in range(n):
    d=input().split(' ')
    #print(d,data)
    p=data.index(int(d[0]))
    data[2*p]=int(d[1])
    data[2*p+1]=int(d[2])
tar=int(input())
#print(data)
out=[]
def ord(i):
    if data[i]==0 or data[i]==-1:
        return
    ord(2*i)
    out.append(data[i])
    ord(2*i+1)
ord(1)
try:
    print(out[out.index(tar)+1])
except:
    print(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    