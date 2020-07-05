n=list(input())
line=[['']*len(n)]*len(n)
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        line[i]=n[i:]+n[0:i]
order=''.line[0]
for i in range(1,len(n)):
    for j in range(0,len(n)-i):
        if ''.line[i]>''.line[i+1]:
            line[i],line[j+1]=line[j+1],line[i]
re=''
for m in range(0,len(n)):
    re+=line[m][len(n)-1]
print(re)
    