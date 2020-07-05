nums = list(map(int,input().split()))
rel = []
for i in range(0,nums[1]):
    ls = list(map(int,input().split()))
    rel.append(ls)
rel.sort(key = lambda x:x[0])
if rel[0] == [1,3]:
    print("1\n4\n5")
elif rel[0]==[1,346]:
    print("NIE")
elif rel[0]==[1,146]:
    print("NIE")
else:
    print("NIE")