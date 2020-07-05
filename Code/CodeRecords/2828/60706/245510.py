n=int(input())
h=input().split(' ')
h_n=[]
for i in range(n):
    h_n.append(int(h[i]))
dollar=h_n[0]
power=0
for i in range(n-1):
    if h_n[i]>=h_n[i+1]:
        power=power+h_n[i]-h_n[i+1]
    else:
        if (h_n[i+1]-h_n[i])>power:
            dollar=dollar+(h_n[i+1]-h_n[i])-power
            power=0
        else:
            power=power-(h_n[i+1]-h_n[i])
print(dollar)
        