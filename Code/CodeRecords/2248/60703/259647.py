N  = int(input())
A  =int(input())
B = int(input())
n = 0
current = 1
while True:
    if(current%A ==0 or current%B==0):
        n+=1

    if(n==N):
        break
    current += 1

print(current%int(pow(10,9)+7))