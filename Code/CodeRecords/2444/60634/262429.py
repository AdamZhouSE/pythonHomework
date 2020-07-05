def solve(nums,k,t):
    i = 0
    while i < len(nums):
        j = i+1
        while j - i <= k and j < len(nums):
            if abs(nums[i] - nums[j])<=t:
                print("true")
                return True
            j += 1
        i += 1
    print("false")
    return False
    
#main-----
temp = input()
nums = []
k = 0
t = 0
i = 0
while i < len(temp):
    if temp[i] == '[':
        arr = ""
        while temp[i] != ']':
            arr += temp[i] 
            i += 1
        arr += temp[i]
        nums = eval(arr)
        i += 1
    if temp[i] == 'k':
        kn = ""
        i += 4
        while temp[i] != ',':
            kn += temp[i]
            i += 1
        k = int(kn)
    if temp[i] == 't':
        tn = ""
        i += 4
        while i < len(temp):
            tn += temp[i]
            i += 1
        t = int(tn)
        break
    i += 1

solve(nums,k,t)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        