

arr=list(map(int, input().strip("[|]").split(",")))
arr_ori=arr.copy()

arr.sort()

st=0

count=0

for i in range(len(arr)):

    end=i+1

    s_ori=set(arr_ori[st:end])

    s_arr=set(arr[st:end])

    if(len(s_ori & s_arr)==end-st):

        st=i+1

        count=count+1
print(count)