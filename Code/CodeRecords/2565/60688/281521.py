numlist1:list=eval("["+input()+"]")
numlist2:list=eval("["+input()+"]")
numlist1.extend(numlist2);
numlist1.sort();
zhognweishu=0;
if len(numlist1)%2==1:
    zhognweishu=numlist1[len(numlist1)//2]
else:zhognweishu=(numlist1[len(numlist1)//2]+numlist1[len(numlist1)//2-1])/2;
print(zhognweishu)
