def subsets(arr:list,k:int):
    re = []
    for i in range(len(arr)-k+1):
        a = list(arr[i:i+k])
        a.sort()
        re.append(a[-1])

    return re

n = eval(input())
for i in range(n):
  line = input().split(' ')
  k = int(line[1])
  arr = list(map(int,input().split(' ')))
  re = subsets(arr,k)
  print(' '.join(map(str,re))+' ')
