N=int(input())
string=str(bin(N))[2:].split('1')[1:-1]
max=-1
for i in string:
    if len(i)>max:
        max=len(i)
max+=1
print(max)