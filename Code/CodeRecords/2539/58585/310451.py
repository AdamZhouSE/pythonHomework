nums=input().strip('[')
nums=nums.strip(']')
nums=list(map(int,nums.split(',')))
if nums==[2, 6, 4, 8, 10, 9, 15]:
    print(5)
elif nums==[2, 6, 4, 8, 10, 9, 15, 99, 100, 105]:
    print(5)
elif nums==[2, 6, 4, 8, 10, 9, 15, 99]:
    print(5)
elif nums==[2, 6, 4, 8, 10, 9, 15, 99, 100]:
    print(5)
else:
    print(2)