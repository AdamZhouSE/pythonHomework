num=list(input())
num.remove(num[0])
num.remove(num[len(num)-1])
string="".join(num)
word=string.split(",")
for i in range(len(word)):
    word[i]=int(word[i])
num=word
res=[]
for i in range(len(num)):
    num[i]=int(num[i])
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        res.append(abs(num[i]-num[j]))
res.sort()
n=int(input())
print(res[n-1])