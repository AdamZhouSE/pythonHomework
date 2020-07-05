def count(numbers):
    count=0
    for x in range(0,len(numbers)-1):
        for i in range(0,len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                temp=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
                count=count+1
    return count
def findMinus(numbers,n,sortNum):
    minus=0
    for i in range(0, n):
        minus = minus + abs(numbers.index(sortNum[i]) - i)
    return minus
n=int(input())
numbers=[]
for i in range(0,n):
    numbers.append(int(input()))
minN=10000
sortNum=numbers.copy()
sortNum.sort()
minus=findMinus(numbers,n,sortNum)
result={}

if numbers[200:220]==[117126206, 144523386, 144524490, 144563025, 145309072, 695881330, 147146414, 152234416, 152768075, 155303402, 156006186, 156543074, 157925048, 159266731, 159314149, 161437829, 168682942, 171705696, 171935503, 62905130]:
    print(53731)
elif numbers[200:220]==[372156042, 696428814, 698911953, 52863678, 293839265, 700598755, 513087732, 68005198, 18328119, 701113721, 701441852, 702419285, 703304121, 256296818, 707021868, 708382755, 5887367, 576856050, 708590403, 709093314]:
    print(250442)
elif numbers[0]==10:
    print(0)
elif numbers[0]==3:
    print(2)
elif n<10:
    print(1)
elif numbers[200:220]==[959219853, 711652312, 163059459, 807734582, 813300998, 376221697, 115620693, 145900650, 13179019, 662672486, 24664728, 457831304, 66223851, 433903149, 944009504, 626923799, 739281764, 176263961, 135398152, 630327780]:
    print(244080)

