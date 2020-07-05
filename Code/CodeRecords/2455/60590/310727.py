n=int(input())
s=list(input())
l=len(s)
if s[l-1]==" ":
    del s[l-1]
st="".join(s)
num=list(map(int,st.split(" ")))
index=[]
for i in range(0,n):
    index.append([])
for i in range(0,n-1):
    s=list(input())
    l=len(s)
    if s[l-1]==" ":
        del s[l-1]
    st="".join(s)
    a,b=map(int,st.split(" "))
    index[a-1].append(b-1)
    index[b-1].append(a-1)
for i in range(0,n):
    if len(index[i])==1 and num[i]<0:
        t=(index[index[i][0]]).index(i)
        del index[index[i][0]][t]
        num[i]=0
sum=0
for i in range(0,n):
    sum+=num[i]
print(sum,end="")