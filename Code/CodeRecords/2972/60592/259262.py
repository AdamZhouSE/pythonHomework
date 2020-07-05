tests = int(input())
for i in range(0,tests):
    s1 = input()
    s2 = input()
    if len(s1) == len(s2):
        if s1 == s2:
            print("Yes")
        else:
            print("No")
    else:
        for j in range(0,len(s1)):
            if s1[j]!=s2[j]:
                if s2[j]==s2[j-1] and s2[j+1]==s1[j]:
                    print("No")
                else:
                    print("Yes")
                break
            if j==len(s1)-1:
                if s2[j+1]==s2[j]:
                    print("No")
                else:
                    print("Yes")