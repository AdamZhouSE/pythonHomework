house = list(map(int,input().split(",")))
heaters = list(map(int,input().split(",")))
m = n = 0
house.sort()
heaters.sort()
result = 0
for temp in house:
    if(n < len(heaters) - 1):
        while(temp > (heaters[n] + heaters[n+1])/2):
            n = n + 1
            if(n >= len(heaters) - 2):
                break
    result = max(result,abs(heaters[n]-temp))
print(result)