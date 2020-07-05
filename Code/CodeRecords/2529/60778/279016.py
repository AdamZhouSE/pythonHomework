def permutations(arr, position, end,res):
    if position == end:
        res.append("".join(arr))
    else:
        for index in range(position, end):
            c=arr[index]
            arr[index]=arr[position]
            arr[position]=c
            permutations(arr, position+1, end,res)
            c=arr[index]
            arr[index]=arr[position]
            arr[position]=c
    if(position==0):
        return res
def is_result(i):
    while(i>1):
        if(i%2==1):
            return False
        i/=2
    return True

string=list(input())
res=[]
res=permutations(string,0,len(string),res)
output="false"
for i in res:
    if(is_result(int(i)) and i[0]!='0'):
        output="true"
        break;
print(output)