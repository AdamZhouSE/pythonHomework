from functools import reduce
def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

li = input().split(",")
dic = {}
for i in li:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(reduce(gcd,dic.values())>1)
