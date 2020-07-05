total = int(input())
sum = 1
data = list(map(int,input().split(' ')))
data.sort()
for i in range(2,data[0]):
    if data[0]%i==0 and data[total-1]%i==0 and data[1]%i==0:
        for j in range(0,total):
            if data[j]%i!=0:
                break
            if j == total-1:
                sum+=1
print(sum)