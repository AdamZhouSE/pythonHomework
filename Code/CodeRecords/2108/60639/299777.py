n=int(input())
number=0
for i in range(n+1):
    string=[j for j in str(i)]
    number+=string.count('1')
print(number)