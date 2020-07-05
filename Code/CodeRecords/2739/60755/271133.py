def judge(num,target):
    s = list(str(num))
    al = 0
    for i in s:
        if i=="0":
            return False
        al = al + int(i)
        if s.count(i)!=1:
            return False
    if al == target:
        return True
    else:
        return False


s = input()
k = s[0]
n = s[-1]
res = ""
m = ""
result=[]
for i in range(1,int(k)+1):
    res = res + str(i)
    m = m + "9"
num = int(res)
while num!=int(m):
    if judge(num,int(n)):
        temp = []
        for i in str(num):
            temp.append(int(i))
        temp.sort()
        if result.count(temp)==0:
            result.append(temp)
    num = num + 1
print(result)   