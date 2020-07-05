first = list(map(int,input().split()))
n = first[0]
k = first[1]
a = list(input().split())
alllucky = [4,7,44,47,74,77,444,447,474,477,744,747,774,777,4444,4447,4474,4477,4744,4747,4774,4777,7444,7447,7474,7477,
            7744,7747,7774,7777]
c = []
count2 = 0
for i in a:
    count = 0
    count = count + i.count('4') + i.count('7')
    c.append(count)
for i in c:
    if i <= k:
        count2+=1
print(count2)        
   