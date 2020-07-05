num = int(input())
stones = input()
res = 0
i = 0
while i<num:
    while i<num-1 and stones[i]==stones[i+1]:
        i+=1
        res+=1
    i+=1
print(res)