arr=eval(input())
standard=sorted(arr)
num=0
beginning=0
ending=1
while ending<=len(arr):
    tempStandard=standard[beginning:ending]
    currentArr=arr[beginning:ending]
    if sorted(currentArr)==sorted(tempStandard):
        beginning=ending
        ending=beginning+1
        num+=1
    else:
        ending+=1
print(num)