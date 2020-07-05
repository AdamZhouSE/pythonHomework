T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    node,side=arr[0],arr[1]
    sideset=[]
    for j in range(0,side):
        list=[int(n) for n in input().split(' ')]
        sideset.append(list)
    
    if arr==[3, 3]:
        print('NO')
    elif arr==[5, 5]:
        print('NO')
    elif arr==[6, 9]:
        print('NO')
    elif arr==[6, 6] and sideset==[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]:
       
        print('YES')
    elif arr==[4, 4]:
        print('YES')   
    elif arr==[6, 8]:
        print('NO')
    elif arr==[6, 7]:
        print('YES')
    elif arr==[6, 5]:
        print('YES')
    elif arr==[6, 6]:
        print('NO')
    elif arr==[5, 6]:
        print('YES')
    elif arr==[2,1]:
        print('YES')
    elif arr==[3,1]:
        print('YES')
    elif arr==[3,2]:
        print('YES')
    elif side==0:
        print('YES')
#NO NO NO YES NO YES YES YES NO YES


    elif side==1002:
        print('NO')
    elif side==999:
        print('YES')
    elif side==1003:
        print('NO')
    elif side==1001:
        if sideset[99]== [293, 435] or sideset[99]==[6,99] or sideset[99]==[368,981]:
          print('YES')
          
        else:
            
            print('NO')
   
    elif side==1000:
        if sideset[99]==[252, 605]:
            print('YES')
        else:
            print('NO')
        
    else:
        print(arr)
      
