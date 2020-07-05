word=list(input())
balance=0
for i in range(len(word)-1):
    if i==0 and word[i]==")":
        print("NO")
        break
    if word[i]=="(":
        balance=balance+1
    if word[i]==")":
        balance=balance-1
        if balance<0:
            print("NO")
            break
if word[i]=="@" and balance==0:
    print("YES")
else:
    print("NO")