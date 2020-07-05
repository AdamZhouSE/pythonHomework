import math
repo = ['Billion','Million','Thousand']
map1 = {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine',
       '10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen',
       '16':'Sixteen','17':'Seventeen','18':'eighteen','19':'Nineteen'}
map2={'2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
src = input()
l = len(src)
high = l % 3
nums = []
if high > 0:
    nums.append(src[0:high])
for i in range(high,l-2,3):
    nums.append(src[i:i+3])
index = 4-math.ceil(l/3)
ans = []
for num in nums:
    if len(num) == 3:
        ans.append(map1[num[0]])
        ans.append('Hundred')
        num=num[1:]
    if len(num) == 2:
        if num[0] == '1':
            ans.append(map1[num])
        else:
            ans.append(map2[num[0]])
            ans.append(map1[num[1]])
    else:
        ans.append(map1[num])
    if index < 3:
        ans.append(repo[index])
    index += 1
print(*ans)
