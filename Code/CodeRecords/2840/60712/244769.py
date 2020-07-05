list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
sum = 0
for i in range(list1[0]):
    if len(str(list2[i]))<=list1[1]:
        sum=sum+1
    else:
        s = str(list2[i])
        temp = 0
        for j in range(len(s)):
            if s[j:j+1] =="4" or s[j:j+1] =="7":
                temp = temp+1
        if temp <=list1[1]:
            sum=sum+1
print(sum)
                