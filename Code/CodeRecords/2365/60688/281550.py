from functools import cmp_to_key
times=int(input());
results=[];
for _ in range(times):
    nums= input();
    temp=input().split(" ");
    key=cmp_to_key(lambda x,y:int(y+x)-int(x+y));#自定义排序算法！！！
    temp = sorted(temp, key=key);
    results.append("".join(temp))
for i in results:
    print(i);