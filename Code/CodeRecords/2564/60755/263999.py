
string = input()
k = int(input())
x = int(input())
l = string[1:-1].split(",")
num = []
for i in l:
    num.append(int(i))
min = 10000
for i in range(len(l)-k+1):
    if abs(sum(num[i:i+k])-k*x) < min:
        min = abs(sum(num[i:i+k])-k*x)
for i in range(len(l)-k+1):
    if abs(sum(num[i:i+k])-k*x) == min:
        print(num[i:i+k])
        break