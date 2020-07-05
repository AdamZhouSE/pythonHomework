cin = input()
left = 7
index = 0
while cin[index]!=']':
    index += 1
right = index
nums = eval(cin[left:right+1])

index+=2
while cin[index]!=',':
    index+=1
sec = index
k = eval(cin[right+6:sec])
t = eval(cin[sec+5:])

re = True
for i in range(len(nums)-k):
    if abs(nums[i]-nums[i+k]) > t:
        re = False
        break
if re:
    print('true')
else:
    print('false')
