import math
def noEmpty(s:str):
    return s and s.strip()

arr1=list(filter(noEmpty,input()[2:-2].split("],[")))
K=int(input())
ans=[]
for i in arr1:
    ans.append(list(map(int,i.split(","))))
ans.sort(key=lambda x:math.sqrt(x[0]*x[0]+x[1]*x[1]))
print(ans[:K])