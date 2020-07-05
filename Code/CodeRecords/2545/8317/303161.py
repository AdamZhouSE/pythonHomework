def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        arr = [int(i) for i in input().split(' ')]
        calc(arr, n)


  
def calc(arr,n): 
    s = set() 
  
    sum = 0
    for i in range(n): 
        sum += arr[i] 
  
        if sum == 0 or sum in s: 
            print('Yes')
            return True
        s.add(sum) 
          
    print('No')
    return False

solve()
