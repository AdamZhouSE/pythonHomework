a=input().split(" ")
n=int(a[0])
m=int(a[1])
str=input()
if(len(str)!=n):
    print("Wrong Input!!!")
else:
    for i in range(m):
        nums = list(map(int, input().split()))
        str1=str[nums[0]-1:nums[1]]
        str2=str[nums[2]-1:nums[3]]
        shorterlen=min(len(str1),len(str2))
        count=0
        for i in range(shorterlen):
            if(str1[i]==str2[i]):
                count+=1
            else:break
        print(count)


