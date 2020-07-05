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

          
#作者：zhu-xiao-xiao-xiao-xiao
#链接：https://leetcode-cn.com/problems/check-if-it-is-a-good-array/solution/pythonli-yong-gcd-by-zhu-xiao-xiao-xiao-xiao/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。