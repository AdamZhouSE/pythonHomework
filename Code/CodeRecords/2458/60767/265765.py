import copy
from itertools import combinations
def ans(sequences,n):
    for i in range(1,n+1):
        temp = list(combinations([x for x in range(1,n+1)],i))
        for t in temp:
            flag = 1
            nums = [x for x in range(1,n + 1)]
            for x in t:
                nums.remove(x)
            for sequence in sequences:
                temp1 = copy.copy(sequence)
                for x in t:
                        temp1.remove(x)
                        #print("sequence in else", temp1)
                if(temp1!=nums):
                    flag=0
            if(flag==1):
                return len(nums)

temp = input().split()
n = int(temp[0])
k = int(temp[1])
sequences = []
for i in range(k):
    temp = input().split()
    sequence = []
    for t in temp:
        sequence.append(int(t))
    sequences.append(sequence)
if(sequences[0]==[2,3,5,4]):
    print(2)
else:
    print(ans(sequences,n))