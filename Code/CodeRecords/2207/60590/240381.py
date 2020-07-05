def cal(num):
    if num==0 or num==1:
        return 1
    count=0
    for i in range(1,num+1):
        if count>num:
            return i-2
        else:
            count+=i

t = int(input())
for i in range(t):
    scanner=input()
    target=int(scanner.split(' ')[0])
    nums=int(scanner.split(' ')[1])
    # if(cal(target)==None):
    #     print(scanner)
    if nums<=0:
        print('0')
    if cal(target)>=nums:
        print('1')
    else:
        print('0')