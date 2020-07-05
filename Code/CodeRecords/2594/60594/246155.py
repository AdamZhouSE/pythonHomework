n=(int)(input())
for index in range(n):
    s=input()
    max=-1
    for index in range(len(s)):
        for index1 in range(index+1,len(s)):
            if s[index1]==s[index]:
                changdu=index1-1-index
                if changdu>max:
                    max=changdu
    print(max)