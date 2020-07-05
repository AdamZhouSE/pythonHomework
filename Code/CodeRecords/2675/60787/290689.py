t=int(input())
for ex in range(0,t):
    s=input()
    true=list(s)
    for i in range(0,len(true)):
        if true[i]=="6":
            true[i]="9"
    print(int("".join(true))-int(s))