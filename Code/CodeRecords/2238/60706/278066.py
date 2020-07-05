import collections
list1=input().split(',')
answers=[]
for i in range(len(list1)):
    answers.append(int(list1[i]))
count = collections.Counter(answers)
ans=sum(-v % (k+1) + v for k, v in count.items())
print(ans)