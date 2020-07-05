n = int(input())
nums = list(map(int,input().split()))
list1 = []*100
nums.sort()

a = nums[0]
b = nums[n-1]
r = 1
q = 1
while(r!=0):
    r = a%b
    if r == 0:
        q = b
    else:
        a=b
        b=r
if q ==1:
    print(1)
else:
    bl = True
    while(bl):
        if q%2==0:
            list1.append(2)
            q=int(q/2)
            if q==1:
                break
        else:
            for i in range(3,q+1,2):

                 if i == q or i>=int(pow(q,0.5)+1):
                    list1.append(q)
                    bl = False
                    break
                 if q%i==0:
                    q = int(q/i)
                    list1.append(i)
                    break
    list2 = []*50

    for i in range(len(list1)):
        bl2=True

        for j in range(len(nums)):
            if nums[j]%list1[i]!=0:
                bls =False
                break
        if bl2:
            list2.append(list1[i])

    preNum=list2[0]
    result=1
    sum1 = 0

    for i in range(len(list2)):
        if preNum==list2[i]:
            sum1=sum1+1
        if  preNum!=list2[i]:
            preNum = list2[i]
            result =result*(sum1+1)
            sum1 = 1
        if i ==len(list2)-1:
            result =result*(sum1+1)
    print(result)



