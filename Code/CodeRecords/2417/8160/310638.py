import math;
def isGoodArray( nums) :
    return __import__("functools").reduce(math.gcd, nums) == 1
line = input().split(',');
#print(line);
arr = [];
for i in range(len(line)):
    arr.append( int(line[i]) );
#print(arr);
print(isGoodArray(arr));

          
