testNum=int(input())
for i in range (testNum):
    rawInputs=input().split(' ')
    size1=int(rawInputs[0])
    size2=int(rawInputs[1])
    sum=int(rawInputs[2])
    rawInputs1=input().split(' ')
    rawInputs2 = input().split(' ')
    arr1=[]
    arr2=[]
    ans=[]
    for rawInput1 in rawInputs1:arr1.append(int(rawInput1))
    for rawInput2 in rawInputs2: arr2.append(int(rawInput2))
    for m in range(size1):
        for n in range (size2):
            if(arr1[m]+arr2[n]==sum):
                ans.append([arr1[m],arr2[n]])
    num=len(ans)
    if(num==0):print('-1')
    else:
        for s in range (num):
            print(' '.join(str(t)for t in ans[s]))