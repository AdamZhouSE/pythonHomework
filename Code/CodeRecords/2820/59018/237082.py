n=int(input())
c=[]
for i in range(n):
    x=input().split(' ')
    c.append('#'.join(x))
dict={}
for j in c:
    if j not in dict.keys():
        dict[j]=1
    else:
        dict[j]=dict[j]+1
print(max(dict.values()))    
        
    