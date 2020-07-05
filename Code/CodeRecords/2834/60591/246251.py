def sortByValue(num):
    return dic[num]

n,m = list(map(int,input().split(" ")))
answers = []
while(n != 0):
    n = n - 1
    answers.append(input())
values = list(map(int,input().split(" ")))
count = 0

for x in range(m):
    dic = {}
    for answer in answers:
        if(answer[x] in dic):
            dic[answer[x]] += 1
        else:
            dic[answer[x]] = 1
    keys = list(dic.keys())
    keys.sort(key = sortByValue)
    count += values[x]* dic[keys[-1]]
print(count)