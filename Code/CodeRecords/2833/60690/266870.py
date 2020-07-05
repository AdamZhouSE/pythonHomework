num=int(input())
rest=input().split(" ")
cin=input().split(" ")
total_rest=0

for i in range(num):
    cin[i]=int(cin[i])
    total_rest+=int(rest[i])
cin.sort()
if total_rest<=cin[-1]+cin[-2]:
    print("YES")
else:
    print("NO")
