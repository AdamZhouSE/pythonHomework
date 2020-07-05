from fractions import Fraction

nums = eval(input())
n = int(input())-1
out = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if(i!=j and out.count(Fraction(nums[i],nums[j]))==0 ):
            out.append(Fraction(nums[i],nums[j]))
out.sort()
res = [out[n].numerator,out[n].denominator]
print(res)