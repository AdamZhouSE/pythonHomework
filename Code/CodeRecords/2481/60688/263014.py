nums=int(input());
results=[];
for i in range(nums):
    nums=input();#废置
    numslist1 = (input().split(" "));
    numslist2 = (input().split(" "));
    diffss=list(set(numslist1).intersection(set(numslist2)))
    results.append(len(diffss))
for i in results:
    print(i)