num = int(input())
row = list(map(int, input().split()))
flag = 0
for i in range(num):
    if row[row[row[i]-1]-1]-1 == i:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")
