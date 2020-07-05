a = list(map(int, input().split()))
n = a[0]
l = a[1]
r = a[2]
mini = []
maxi = []
allelement = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152]
for j in range(l):
    mini.append(allelement[j])
for i in range(n-l):
    mini.append(1)
for i in range(r):
    maxi.append(allelement[i])
for i in range(n-r):
    maxi.append(allelement[r-1])
print(sum(mini), sum(maxi))
