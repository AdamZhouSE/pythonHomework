#10
n = int(input())
ori1 = input().split(" ")
left = [int(item) for item in ori1]
ori2 = input().split(" ")
cap = [int(item) for item in ori2]
sum = 0
for i in range(0,n):
    sum += left[i]
cap.sort()
capacity = cap[n-1] + cap[n-2]
if(sum>capacity):
    print("NO")
else:
    print("YES")