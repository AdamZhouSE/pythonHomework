c=int(input())
max=int(c**0.5)
flag="False"
for i in range(max+1):
    if ((c-i**2)**0.5)%1==0:
        flag="True"
if flag=="True":
    print(flag)
else:
    print(flag)