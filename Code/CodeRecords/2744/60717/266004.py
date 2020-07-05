def isPalindrome(str1):
    lenn=int(len(str1)/2)
    for i in range(0,lenn):
        if str1[i]!=str1[len(str1)-1-i]:
            return False
    return True

n=int(input())
list1=[]
for i in range(0,n):
    list1.append(input().split()[1])
list2=[]
for i in range(0,n):
    for j in range(0,n):
        list2.append(list1[i]+list1[j])
count=0
for i in list2:
    if isPalindrome(i):
        count+=1
print(count)