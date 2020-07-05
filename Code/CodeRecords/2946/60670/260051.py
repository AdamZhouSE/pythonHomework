def reverse(c):
    if c=="1":
        return "0"
    else:
        return "1"

ori=input()
status="1"
n=0
for i in range(len(ori)-1,-1,-1):
    if ori[i]!=status:
        n+=1
        status=reverse(status)
print(n,end="")