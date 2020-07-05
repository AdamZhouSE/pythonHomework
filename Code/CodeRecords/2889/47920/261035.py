n = eval(input())
#print(n)
m = 1/n
inp = input().split(" ")
sum = 0
for i in range(n):
    sum = sum + int(inp[i])   
print("{:.6f}".format(sum/n))