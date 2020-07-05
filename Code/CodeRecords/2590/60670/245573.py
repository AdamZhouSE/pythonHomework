vowels=('a','e','i','o','u')
t=int(input())
for i in range(0,t):
    uid=input()
    uid_c=[]
    for c in uid:
        if not((c in vowels)or(c in uid_c)):
            uid_c.append(c)
    if len(uid_c)%2==1:
        print("HE!")
    else :
        print("SHE!")