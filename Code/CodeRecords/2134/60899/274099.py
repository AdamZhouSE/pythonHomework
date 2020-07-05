buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
if buckets == 1 :print(0)
w = minutesToTest / minutesToDie + 1
re = 1
while pow(w, re) < buckets :
    re +=1
print(re)