n=int(input())
arr=[int(x) for x in input().split()]
for i in range(0,n):
	if arr[arr[arr[i]-1]-1]==i+1:
		print("YES")
		exit()
print("NO")