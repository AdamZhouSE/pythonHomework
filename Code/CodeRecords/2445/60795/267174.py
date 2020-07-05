arr=input().split(',')
ss,tt=[],[]
arr[0].lower()
arr[1].lower()
for i in range(5,len(arr[0])-1):
    ss.append(arr[0][i])
for i in range(6,len(arr[1])-1):
    tt.append(arr[1][i])
ss.sort()
tt.sort()
s="".join(ss)
t="".join(tt)
if s==t:
    print("true")
else:
   
    print("false")