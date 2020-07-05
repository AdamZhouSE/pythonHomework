buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
k = minutesToTest / minutesToDie
# print(k)
i = 1
# while pow(2,i)*pow(i,k-1) < buckets: #16*4^3
#     i+=1
while buckets/pow(i,k-1) > pow(2,i):
    i+=1
print(i+1)