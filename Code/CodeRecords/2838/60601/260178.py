n = eval(input())
num = list(map(int,input().split(' ')))
num.sort()
sum = 0
j = n - 1
for i in range(n//2):
    sum += pow(num[i]+num[j],2)
    j = j - 1
print(sum)
