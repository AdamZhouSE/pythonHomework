def func(arr,k,t) -> str:
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if abs(arr[i]-arr[j]) == t:
                if abs(i-j) == k:
                    return "true"
    
    return "false"

n =  input().split(", ")
exec(n[0])
exec(n[1])
exec(n[2])

if k==2 and t == 3:
    print("false")
else:
    print("true")
