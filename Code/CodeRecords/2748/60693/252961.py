def remove_invalid_par(s):
    left_delete,right_delete = 0,0
    for i in range(len(s)):
        if s[i] == '(':
            left_delete+=1
        elif s[i] == ')':
            if left_delete == 0:right_delete += 1
            if left_delete > 0:left_delete -= 1
    helper(s,0,0,0,left_delete,right_delete)
    return list(res)

def helper(s,index,num_left,num_right,left_delete,right_delete):
    if index == len(s):
        if left_delete==0 and right_delete==0:
            res.add(''.join(tmp))
    elif num_right > num_left :
        return
    else:
        ch=s[index]
        if (ch == '(' and left_delete > 0) or (ch == ')' and right_delete > 0):
            if ch == '(':
                helper(s,index+1,num_left,num_right,left_delete-1,right_delete)
            elif ch == ')':
                helper(s,index+1,num_left,num_right,left_delete,right_delete-1)
        tmp.append(ch)
        if ch!='(' and ch != ')':
            helper(s,index+1,num_left,num_right,left_delete,right_delete)
        elif ch==')':
            helper(s, index + 1, num_left , num_right+1, left_delete, right_delete)
        else:
            helper(s, index + 1, num_left+1, num_right, left_delete, right_delete)
        tmp.pop()

str=input()
print(remove_invalid_par(str))