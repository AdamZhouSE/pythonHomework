arr = input()
suffix = []
for i in range(len(arr)):
    suffix.append(arr[i:])
dic = {i:x for i,x in enumerate(suffix,start=1)}
dic = sorted(dic,key = dic.get)
print(*dic)
