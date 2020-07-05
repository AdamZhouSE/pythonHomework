cnt=1
ch=[[0 for i in range(100)] for i in range(100)]
n=0
i=0
while(1):
    try:
        ch[i]=str(input())
        i+=1
        if ch[i]=='9':
            break
        n+=1
    except:
        break
jd=True
for i in range(n):
    for j in range(i+1,n):
        if ch[i].find(ch[j])==0 or ch[j].find(ch[i])==0:
            jd=False
            break
if jd:
    print("Set",cnt,"is immediately decodable")
    cnt+=1
else:
    print("Set",cnt,"is not immediately decodable")
    cnt+=1