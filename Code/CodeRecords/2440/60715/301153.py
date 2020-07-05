num=input("")
num=num[1:len(num)-1]
nums=num.split(',')
nums=list(map(int,nums))
print(sorted(nums))