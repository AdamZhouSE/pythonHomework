chips=eval(input())
oddSum=0
evenSum=0
for i in range(len(chips)):
    if(i%2==0):
        oddSum+=chips[i]
    else:
        evenSum+=chips[i]
if(oddSum>evenSum):
    print(evenSum)
else:
    print(oddSum)