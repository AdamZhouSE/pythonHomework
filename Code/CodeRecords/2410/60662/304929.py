arr = list(map(int,input().split(',')))
difference = int(input())
length = len(arr)
t = 1
dic ={}
for i in range(length):
    if arr[i] - difference in dic:
        dic[arr[i]] = dic[arr[i]-difference]+1
        
    else:
        dic[arr[i]]=1
    t = max(t,dic[arr[i]])
print(t)