a=int(input())
num=0
for i in range(2,a):
        flag=True
        for j in range(2,i):
            if(i%j==0):
                flag=False
                break
        if flag:
            num=num+1
print(num)