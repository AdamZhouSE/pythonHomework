num,d = map(int,input().split())
str = input().split(' ')
lists = [int(i) for i in str]
index = 0
for i in range(num):
    if i==num-1:
        break
    while lists[i]>=lists[i+1]:
        lists[i+1]+=d
        index+=1
print(index)