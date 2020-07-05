isp = {'(':1,'#':0,'+':2,'-':2,'*':3,'/':3,'^':4}
osp = {'(':99,'#':0,'+':2,'-':2,'*':3,'/':3,'^':4}

#main-----
test = int(input())
for t in range(test):
    s = input()
    s += '#'
    stack = ['#']

    i = 0
    while i < len(s):
        if s[i]<='Z' and s[i]>='A' or s[i] <= 'z' and s[i] >= 'a':
            print(s[i],end="")
        elif s[i] == '#':
            while len(stack) != 1:
                temp = stack.pop()
                print(temp,end="")
            break
        elif s[i] == ')':
            temp = stack.pop()
            while temp != '(':
                print(temp,end="")
                temp = stack.pop()
        else:
            temp = stack.pop()
            while isp[temp] >= osp[s[i]]:
                print(temp,end="")
                temp = stack.pop()
            stack.append(temp)
            stack.append(s[i])
        i += 1
    print()