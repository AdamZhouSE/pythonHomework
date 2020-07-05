def func(str):
    left=0
    right=len(str)-1
    while left<right:
        if str[left]!=str[right]: return False
        else: 
            left+=1
            right-=1
    return True
if func(input()): print("True")
else: print("False")    