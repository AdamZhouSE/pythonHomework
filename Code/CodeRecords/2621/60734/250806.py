test = list(map(int,input().split(',')))

#前i项和
formerSum = []
for i in range(len(test)):
    formerSum.append(sum(test[0:i+1]))
print(max(formerSum)-min(formerSum))