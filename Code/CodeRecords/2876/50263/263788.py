n = int(input())
lights = input().split()
count = 0
for i in range(1,n-1):
    if lights[i-1] == '1' and lights[i] == '0'  and lights[i+1] == '1' :
        count+=1
        lights[i+1] = '0'
print(count)