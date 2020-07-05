tests=input()
testlist=[]
for i in range(0,(int)(tests)):
    testlist.append(input())
for test in testlist:
   sum=0
   for i in range(1,(int)(test)+1):

        sum+=pow(i,5)
   print(sum)