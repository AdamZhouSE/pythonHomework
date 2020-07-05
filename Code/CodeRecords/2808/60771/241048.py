#25
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
seq = num[:]
seq.sort()
max1 = seq[n-1]
min1 = seq[0]
index_max = num.index(max1)
index_min = num.index(min1)
print(max(n-1-index_max,n-1-index_min,index_max,index_min))