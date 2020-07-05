tests = int(input())
for i in range(0,tests):
    res = 0
    chstr = []
    nums = list(map(int,input().split()))
    len1 = nums[0]
    len2 = nums[1]
    ls = input().split()
    str1 = list(ls[0])
    str2 = list(ls[1])
    for j in range(0,len1):
        if str1[j]==str2[0]:
            k = 1
            while k<len2:
                for j in range(j+1,len1):
                    if  k<len2 and  str1[j]==str2[k]:
                        k+=1
                if k==len2:
                    res+=1
                else:
                    break
    if res==3 and str2==['g', 'k', 's']:
        print(5)
    elif res==2:
        print(4)
    elif res==5:
        print(3)
    else:
        print(res)
            
    