s=input()
n=len(s)
li=[]
for i in range(n):
    li.append(s[i:])
li=sorted(li)
li_num=[]
for i in range(n):
    li_num.append(n+1-len(li[i]))
print(" ".join(map("{}".format,li_num)))