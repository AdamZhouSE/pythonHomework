n = int(input())
string = input()
st=[]
s=0
for i in string:
    st.append(i)
count = 0
for i in range(n):
    if i+1<n and st[i]==st[i+1]:
        count = count + 1
print(count)