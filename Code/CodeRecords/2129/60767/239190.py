def integerReplacement(num):
    if(num==1):
        return 0
    if(num%2==0):
        return integerReplacement(num/2)+1
    if(num%2==1):
        return min(integerReplacement(num-1)+1, integerReplacement(num+1)+1)

num = int(input())
print(integerReplacement(num))