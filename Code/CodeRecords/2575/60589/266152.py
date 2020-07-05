def find_depth():
    s=input()
    stack1=[]
    stack2=[]
    ans=[]
    odd_or_even=[]
    for c in s:
        if c == '(':
            if len(stack1) <= len(stack2):
                stack1.append(c)
                ans.append(0)
                odd_or_even.append(0)
            else:
                stack2.append(c)
                ans.append(1)
                odd_or_even.append(1)
        else:
            if odd_or_even.pop()==0:
                ans.append(0)
                stack1.pop()
            else:
                ans.append(1)
                stack2.pop()
    print(ans)

    
find_depth()