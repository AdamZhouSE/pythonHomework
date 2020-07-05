def judge(str1):
    tempres = '';
    s = len(str1)
    if ((s == 1)|(str1[0]=='0')):
        return ge[str1[0]]
    else:
        if (str1[0] == '1'):
            return teen[str1[1]]
        else:
            if(str1[1]!='0'):
                tempres = shi[str1[0]] + " " + ge[str1[1]]
            else:
                tempres = shi[str1[0]]
            return tempres
    pass
ge={'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
shi={'0':'','1':'Ten','2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
teen={'0':'Ten','1':'Eleven','2':'Twelve','3':'Thirteen','4':'Fourteen','5':'Fifteen','6':'Sixteen','7':'Seventeen','8':'Eighteen','9':'Nineteen'}
danwei={1:'Thousand',2:'Million',3:'Billion'}
num_str=str(input())
res=''
temp=''
substr_list=[]
s=len(num_str)
shang=s//3
yushu=s%3
for i in range(0,shang+1):
    tempres = ''
    if i!=shang:
        temp=num_str[s-3:s]
        s=s-3
        tempres=judge(temp[-2:])
        if tempres!='':
            if(temp[0]!='0'):
                tempres=ge[temp[0]]+' '+'Hundred'+' '+tempres
        else:
            if (temp[0] != '0'):
                tempres = ge[temp[0]] + ' ' + 'Hundred'
    else:
        if yushu==1:
            tempres=judge(num_str[0])
        elif yushu==2:
            tempres=judge(num_str[0:2])
    if tempres!='':
        if i!=0:
            res=tempres+' '+danwei[i]+' '+res
        else:
            res=tempres
print(res)

