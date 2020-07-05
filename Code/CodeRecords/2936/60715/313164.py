N=int(input())
st=[]
while N>0:
    s=input()
    ss=""
    for i in s:
        if i != '-':
            ss+=i;
    st.append(ss)
    N-=1
oo=0
for i in range(len(st)-1):
    count=0
    for j in range(1,len(st)):
        if st[i]==st[j]:
            count+=1
            oo+=1
    if count>1:
        re=st[i][0:3]+"-"+st[i][3:]
        print(re,end=' ')
        print(count)
if oo==0:
    print("No duplicates.",end='')