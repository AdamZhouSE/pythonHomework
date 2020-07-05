def is_palindromic(num):
    return num == num[::-1]

n=int(input())
zfc=[]
for i in range(n):
    row=input().split()
    zfc.append(row[1])
oc=[]
for i in zfc:
    for j in zfc:
        oc.append(i+j)
final=0
for i in oc:
    if is_palindromic(i):
        final+=1
print(final)