s = input().split()
numOfBa = int(s[0])
length = int(s[1])
barrels = list(map(int,input().split(' ')))
max = 0
for ba in barrels:
    if(length % ba == 0):
        max = int(length / ba)
print(max)