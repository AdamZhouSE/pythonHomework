n=int(input())
for q in range(n):
    s1=input()
    s2=input()
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                print(s1[i])
                break
        if i==len(s1)-1:
            print("$")
            break
        