import sys
s=sys.stdin.read()
sli=s.split("=")
leftx=0
leftnum=0
rightx=0
rightnum=0
left=sli[0]
right=sli[1]
for i in range(len(left)):
    if i==0 and left[i]=='x':
        leftx+=1
    elif i==0 and left[i]>='0' and left[i]<='9':
        num = ""
        while left[i] >= '1' and left[i] <= '9':
            num += left[i]
            i += 1
            if i >= len(left) - 1:
                break
        nums = int(num)
        if i > len(left) - 1:
            i -= 1
        if left[i] == 'x':
            leftx += nums
        else:
            leftnum += nums
            if i < len(left) - 1:
                i -= 1
    elif left[i]=='-':
        if left[i+1]=='x':
            leftx-=1
        else:
            i+=1
            num=""
            while left[i]>='1' and left[i]<='9' :
                num+=left[i]
                i+=1
                if i>=len(left)-1:
                    break
            nums=int(num)
            if left[i]=='x':
                leftx-=nums
            else:
                leftnum-=nums
                if i<len(left)-1:
                    i-=1
    elif left[i]=='+':
        if left[i+1]=='x':
            leftx+=1
        else:
            i+=1
            num=""
            while left[i]>='1' and left[i]<='9' :
                num+=left[i]
                i+=1
                if i>=len(left)-1:
                    break
            nums=int(num)
            if i>len(left)-1:
                i-=1
            if left[i]=='x':
                leftx+=nums
            else:
                leftnum+=nums
                if i<len(left)-1:
                    i-=1
for i in range(len(right)):
    if i==0 and right[i]=='x':
        rightx+=1
    elif i==0 and right[i]>='0' and right[i]<='9':
        num = ""
        while right[i] >= '1' and right[i] <= '9':
            num += right[i]
            i += 1
            if i >= len(right) - 1:
                break
        nums = int(num)
        if right[i] == 'x':
            rightx += nums
        else:
            rightnum += nums
            if i < len(right) - 1:
                i -= 1
    elif right[i]=='-':
        if right[i+1]=='x':
            rightx-=1
        else:
            i+=1
            num=""
            while right[i]>='1' and right[i]<='9' :
                num+=right[i]
                i+=1
                if i>=len(right)-1:
                    break
            nums=int(num)
            if i>len(right)-1:
                i-=1
            if right[i]=='x':
                rightx-=nums
            else:
                rightnum-=nums
                if i<len(right)-1:
                    i-=1
    elif right[i]=='+':
        if right[i+1]=='x':
            rightx+=1
        else:
            i+=1
            num=""
            while right[i]>='1' and right[i]<='9' :
                num+=right[i]
                i+=1
                if i>=len(right)-1:
                    break
            nums=int(num)
            if i>len(right)-1:
                i-=1
            if right[i]=='x':
                rightx+=nums
            else:
                rightnum+=nums
                if i<len(right)-1:
                    i-=1
if leftx==rightx:
    if leftnum==rightnum:
        print("Infinite solutions")
    else:
        print("No solution")
else:
    fenzi=rightnum-leftnum
    fenmu=leftx-rightx
    res=fenzi//fenmu
    print("x="+str(res))