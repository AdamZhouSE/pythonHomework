
n = int(input())
binary = []
while(n!=0):
    binary.append(int(n%2))
    n = int(n/2)
    
for i in range(len(binary)):
    if(binary[i] == 1):
        binary[i] = 0
    else:
        binary[i] = 1
re = 0
for i in range(len(binary)):
    if(binary[i]==1):
        re += 2**i
print(re)
