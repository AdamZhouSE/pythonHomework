
def toggleBitsFromLToR(n,l,r): 
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
    return (n ^ num) 
n = 50
l = 2
r = 5
  
print(toggleBitsFromLToR(n, l, r)) 
  
# This code is contributed 
# by Anant Agarwal. 