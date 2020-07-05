import math
A=int(input())


def change(give):
    M=['', 'M','MM','MMM']
    C=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    X=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    I=['','I','II','III','IV','V','VI','VII','VIII','IX']
    return M[give//1000]+C[(give%1000)//100]+X[(give%100)//10]+I[give%10]
print(change(A))