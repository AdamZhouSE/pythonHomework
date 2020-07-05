a=input()
b=input()

sum=0
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)]==b:
        sum+=1

print(sum,end="")