binary=list(input())
three=list(input())
target=[]
for i in range(len(binary)):
    a=binary.copy()
    if(a[i]=="1"):
        a[i]="0"
    else:
        a[i]="1"
    target.append(a)
targets=[]
print(bin(1))
for i in target:
    targets.append(int("0b"+"".join(i)))
print(targets)