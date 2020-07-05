cases=int(input())
prime_nums=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for i in range(cases):
    n=int(input())
    print(pow(prime_nums[n-1],2)+1)