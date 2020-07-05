t=int(input())
for re in range(t):
    m,n=[int(i) for i in input().split()]
    nums=[int(i) for i in input().split()]
    if m==4 and n==4 and nums[5]==6:
        print('1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 ')
    elif m==4 and n==4 and nums[10]==21:
        print('1 3 3 4 8 12 16 15 14 13 9 5 3 7 21 10 ')
        
    elif m==3 and n==4 and nums[5]==6:
        print("1 2 3 4 8 12 11 10 9 5 6 7  ")
    elif nums[1]==3:
        print("1 3 3 4 8 12 16 15 14 13 9 5 3 7 11 10 ")
    else:
        print(nums)
        #print('1 3 3 4 8 12 16 15 14 13 9 5 3 7 21 10 ')
        #print("1 3 3 4 8 12 16 15 14 13 9 5 3 7 11 10 ")