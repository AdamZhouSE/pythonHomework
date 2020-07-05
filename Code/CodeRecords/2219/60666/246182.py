c=int(input())
max=int(c**0.5)
for i in range(max+1):
    if ((c-i**2)**0.5)%1==0:
        flag="True"
    flag="False"
print(flag)