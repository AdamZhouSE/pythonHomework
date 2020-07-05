nList = [int(i) for i in list(input().strip().lstrip('0'))]
nList = [nList[max(i, 0):i + 3:] for i in range(len(nList) % 3 - 3, len(nList), 3) if i + 3 != 0]
dict1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
dict2 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
dict3 = ['', None, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
dict4 = [' Billion', ' Million', ' Thousand', '']
H = ' Hundred'
for l in nList:
    if len(l) == 1:
        l[0] = dict1[l[0]]
        continue
    elif len(l) == 3:
        l[0] = dict1[l[0]]
        if l[0] != '':
            l[0] += H
    if l[-2] == 1:
        l[-2] = ''
        l[-1] = dict2[l[-1]]
    else:
        l[-2] = dict3[l[-2]]
        l[-1] = dict1[l[-1]]
for i in range(len(nList)):
    nList[i] = ' '.join(j for j in nList[i] if j != '')
for i in range(2, len(nList) + 1):
    if nList[-i] != '':
        nList[-i] += dict4[-i]
print(' '.join(' '.join(nList).split()))