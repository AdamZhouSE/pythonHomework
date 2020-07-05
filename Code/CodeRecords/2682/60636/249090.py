
def toggleBitsFromLToR(n,l,r): 
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
    return (n ^ num) 
n = 8
l = 1
r = 2
  
print(toggleBitsFromLToR(n, l, r)) 
  
# This code is contributed 
# by Anant Agarwal. 