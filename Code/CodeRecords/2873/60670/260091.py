n,m=map(int,input().split())
line=input().split()
b=input().split()
key=""
for c in line:
    if c in b:
        key+=c
print(key)