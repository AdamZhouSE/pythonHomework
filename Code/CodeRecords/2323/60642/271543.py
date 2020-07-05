nums = [int(i) for i in input().split(',')]
k = int(input())
diff = max(max(nums)-min(nums)-k*2,0)
print(diff)