tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(int(input()))
res=[]
for i in range(4,pow(10,7)):
    temp=list(str(i))
    if temp.count('4')+temp.count('7')==len(temp):
        res.append(i)
for i in lists:
    print(res[i-1])