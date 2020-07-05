n = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
x = minutesToTest//minutesToDie+1
i = 1
while pow(x,i)<n:
    i+=1
print(i)
