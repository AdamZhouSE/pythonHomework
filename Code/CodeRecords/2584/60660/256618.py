n=int(input())
if(n%4==0):#先手的话1,2,3一定能拿完，4拿1，2，3剩下的都在3以内，5拿走1个变成4个对方先手的问题即对面不可能赢，以此类推
    print(False)
else:
    print(True)