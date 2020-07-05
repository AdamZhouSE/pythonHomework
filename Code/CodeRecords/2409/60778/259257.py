chips=eval(input())
oddSum=0
evenSum=0
for i in chips:
    if(i%2==0):
        oddSum+=1
    else:
        evenSum+=1
if(oddSum>evenSum):
    print(evenSum)
else:
    print(oddSum)