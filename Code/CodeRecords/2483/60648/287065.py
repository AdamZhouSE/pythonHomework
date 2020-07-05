n=int(input())
for q in range(n):
    s1=input()
    s2=input()
    tag=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                print(s1[i])
                tag=1
                break
        if i==len(s1)-1:
            print("$")
            break
        if tag==1:
            break
        