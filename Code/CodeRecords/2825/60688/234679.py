times=int(input());
scores={};
for i in range(times):
    numsstr=input().split(" ");
    numbers=[int(x) for x in numsstr];
    sums=sum(numbers);
    scores[i]=sums;
# print(scores)
sortedscore=dict(sorted(scores.items(),key=lambda x:x[1],reverse=True));
keylist=list(sortedscore.keys());
print(keylist.index(0)+1)