n = int(input())
li = [int(x) for x in input().split()]
m = 0
ans = []
sum = 0
for i in range(n):
    # print("i=%d"%i)
    if m>=li[i]:
        ans.append(m)
        m = 1
        sum+=1
    else:
        m = li[i]
    # print("m=%d"%m)
ans.append(m)
print(sum+1)
print(" ".join([str(x) for x in ans]))