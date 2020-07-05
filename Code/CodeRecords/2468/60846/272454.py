def printList(lst):
    #firstFlag=False
    #for num in lst:
     #   if not firstFlag:
      #      firstFlag=True
       #     print(num,end='')
    for num in lst:
        print(num,'',end='')
    print()
t=int(input())
while t:
    n=int(input())
    nums=[int(x) for x in input().split()]
    ret=[]
    product=1
    for i in range(n):
        product*=nums[i]
    for i in range(n):
        ret.append(product//nums[i])
    printList(ret)
    t-=1