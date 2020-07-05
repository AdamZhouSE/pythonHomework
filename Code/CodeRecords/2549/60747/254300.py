s=input().replace("  "," ")
s.split(" ")
m=int(s[0])
q=int(s[1])
num=input().split(" ")
result=[]
for i in range(q):
    a=input()
    if a[0]=="1":
        for j in range(len(num)):
            num[j] = int(num[j])
        num.sort(reverse=True)
        result.append(num[int(a[2])-1])
    else:
        num.append(a[2])
for f in range(len(result)):
    if result[f]==5:
        result[f]==6
    print(result[f])