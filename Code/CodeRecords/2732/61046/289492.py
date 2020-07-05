num=int(input())
test=[]
for i in range(num):
    test.append(input())

for i in range(num):
    res=test[i].split(" ")
    ans=pow(int(res[0]),int(res[1]))
    ans=ans%int(res[2])
    print(str(ans))