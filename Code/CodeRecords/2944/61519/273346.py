word=list(input())
balance=0
for i in range(len(word)-1):
    if word[i]=="(":
        balance=balance+1
    if word[i]==")":
        balance=balance-1
    if balance<0:
        print("NO")
        break
if balance==0:
    print("YES",end="")
else:
    print("NO",end="")