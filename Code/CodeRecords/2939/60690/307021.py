l=input().split(" ")
k,m=int(l[0]),int(l[1])
nums=[1]
newAdd=[]
nextIni=[1]

while len(nums)<2*k:
    for i in range(len(nextIni)):
        a,b=2*nextIni[i]+1,4*nextIni[i]+5
        newAdd.append(a)
        newAdd.append(b)
        nums.append(a)
        nums.append(b)
    nextIni.clear()
    for e in newAdd: nextIni.append(e)
    newAdd.clear()
    nums.sort()

s=""
for i in range(k):
    s+=str(nums[i])
if s=="13":
    print("13")
else:print(s)
ss=[]
for i in range(len(s)):
    ss.append(int(s[i]))
maxNum=0
index=0
for i in range(m+1):
    if ss[i]>maxNum:
        index=i
        maxNum=ss[i]
if index==m:print(s[index:])
else:
    ss_=ss[index+1:]
    for j in range(m-index):
        ss_.pop(ss_.index(min(ss_)))
    string=s[index]
    for e in ss_:string+=str(e)
    print(string,end="")
    